import numpy as np
import matplotlib.pyplot as plt

while True:
    try:
        filelocation = input("Copy & paste isotope .npy file path (press enter when done): ").strip('"')
        spectra = np.load(filelocation)
        hist, bins = np.histogram(spectra, bins = 3000)
        plt.plot(range(np.size(hist)), hist)
    except:
        break

plt.show()