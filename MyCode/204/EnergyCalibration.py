import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
from datetime import datetime

spectrarange = 100000

while True:
    isotope = input("Enter name of isotope: ")
    if isotope == '':
        break
    hist = []
    peaklocations = []
    peakheights = []
    energylist = []
    while True:
        try:
            filelocation = input("Enter location of calibration isotope spectra: ").strip('"')
            spectra = np.load(filelocation)
            hist, bins = np.histogram(spectra, bins = spectrarange//20, range = (0, spectrarange))
            peaklocations, _ = find_peaks(hist, distance = 100, prominence = int(np.amax(hist))/10)
            for x in range(np.size(peaklocations)):
                peakheights.append(hist[int(peaklocations[x])])
            peakheights.sort(reverse=True)
            plt.plot(hist, label=filelocation)
            plt.plot(peaklocations, hist[peaklocations], "vk")
            plt.xlim(0)
            plt.legend(loc='upper left')
            plt.show()
            break
        except:
            print("Cannot load file")
    while True:
        try:
            energy = input("Enter energies (in keV) of highest peaks indicated: ")
            energylist.append(float(energy))
        except:
            if energy == '':
                break
            else:
                print('Not a valid energy')
    energylist.sort()
    peakheights2 = peakheights[:len(energylist)]
    with open('calibrationdata.txt', 'a') as f:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write(isotope + ' ' + dt_string + '\n')
        x = 0
        for y in range(np.size(peaklocations)):
            if hist[int(peaklocations[y])] in peakheights2:
                f.write(str(peaklocations[y]) + ' ' + str(energylist[x]) + '\n')
                x += 1
            else:
                pass