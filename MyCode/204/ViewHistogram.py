import numpy as np
from scipy.signal import find_peaks, peak_widths
import matplotlib.pyplot as plt

spectrarange = 100000
calfactor = 1

calfilelocation = input("Enter calibration data .txt file location, or press enter to continue without calibrated energies: ").strip('"')
if calfilelocation != '':
    with open(calfilelocation, 'r') as calfile:
        factorlist = []
        for line in calfile:
            try:
                singlefactor = line.split()            
                factorlist.append(float(singlefactor[0])/float(singlefactor[1]))
            except:
                pass
        print("Cal factors are:")
        print(factorlist)
        calfactor = sum(factorlist)/len(factorlist)

while True:
    try:
        filelocation = input("Enter spectra location: ").strip('"')
        spectra = np.load(filelocation)
        hist, bins = np.histogram(spectra, bins = spectrarange//20, range = (0, spectrarange))
        peaklocations, _ = find_peaks(hist, distance = 10, prominence = int(np.amax(hist))/20)
        FWHM = peak_widths(hist, peaklocations, rel_height = 0.5)
        Xenergy = []
        peaklocations2 = []
        for x in range(np.size(hist)):
            Xenergy.append(x/calfactor)
        for x in range(np.size(peaklocations)):
            if 5 < FWHM[0][x] < 20:
                print(str(peaklocations[x]/calfactor) + ' keV | ' + str(hist[int(peaklocations[x])]) + ' counts | ' + str(FWHM[0][x]) + ' FWHM')
                peaklocations2.append(peaklocations[x])
        np_peaklocations2 = np.array(peaklocations2, dtype = int)
        plt.plot(Xenergy, hist, label = filelocation)
        plt.plot(np_peaklocations2/calfactor, hist[np_peaklocations2], "vk")
    except:
        if filelocation == '':
            break
        else:
            print("Cannot load file")

if calfactor != 1:
    plt.xlabel('Energy in keV')
plt.xlim(0)
plt.legend(loc='upper left')
plt.show()

