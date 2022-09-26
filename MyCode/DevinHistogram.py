import numpy as np
import matplotlib.pyplot as plt

spectra = np.load('spectradata.npy')
resolution = np.amax(spectra)-np.amin(spectra)
plt.hist(spectra, bins=int(resolution), histtype='step')
plt.xlim(left=0)
plt.show()

