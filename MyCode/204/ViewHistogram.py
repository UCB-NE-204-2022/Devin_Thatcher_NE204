import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

spectrarange = 100000

while True:
    try:
        filelocation = input("Enter spectra location: ")
        filelocation = filelocation.strip('"')
        spectra = np.load(filelocation)
        hist, bins = np.histogram(spectra, bins = spectrarange//20, range = (0, spectrarange))
        peaks, _ = find_peaks(hist, prominence = int(np.amax(hist))/8)
        plt.plot(hist, label=filelocation)
        plt.plot(peaks, hist[peaks], "vk")
    except:
        if filelocation == '':
            break
        else:
            print("Cannot load file")

plt.xlim(0)
plt.legend(loc='upper left')
plt.show()

