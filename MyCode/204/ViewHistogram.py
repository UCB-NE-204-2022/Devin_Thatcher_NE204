import numpy as np
import matplotlib.pyplot as plt

while True:
    try:
        filelocation = input("Enter spectra location: ")
        filelocation = filelocation.strip('"')
        spectra = np.load(filelocation)
        resolution = int(np.amax(spectra)/20)
        plt.hist(spectra, bins=resolution, histtype='step', label=filelocation)
    except:
        break

plt.xlim(0)
plt.legend(loc='upper left')
plt.show()

