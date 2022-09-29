import numpy as np
import matplotlib.pyplot as plt

spectra = np.load('spectradata.npy')
spectra2 = np.load('spectradata2.npy')
ratio = float(np.amax(spectra2))/float(np.amax(spectra))
spectraratio = []
for a in range(np.size(spectra)):
    spectraratio.append(spectra2[a]/spectra[a])
ratio = np.average(spectraratio)
for a in range(np.size(spectra)):
    spectra[a]=ratio*spectra[a]
resolution = int(np.amax(spectra)/50)
plt.hist(spectra, bins=resolution, histtype='step', label='raw_data max pulse height')
plt.hist(spectra2, bins=resolution, histtype='step', label='after trapezoidal filter + pole zero correction')
plt.xlim(0, 50000)
plt.legend(loc='upper left')
plt.show()

