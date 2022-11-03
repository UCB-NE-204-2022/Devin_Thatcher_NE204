import numpy as np
from scipy.signal import find_peaks, peak_widths
import matplotlib.pyplot as plt

calfactor = 1

calfilelocation = input("Copy & paste calibration data .txt file path, or press enter to continue without calibrated energies: ").strip('"')
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
        filelocation = input("Copy & paste isotope .npy file path (press enter when done): ").strip('"')
        spectra = np.load(filelocation)
        hist, bins = np.histogram(spectra, bins=5000, range=(0, 1000))
        peaklocations, _ = find_peaks(hist, distance=10, prominence=int(np.amax(hist))/5)
        FWHM = peak_widths(hist, peaklocations, rel_height=0.5)
        Xaxisfactor = []
        peaklocations2 = []
        allFWHM = []
        allheights = []
        resolution = []
        x_label = 'channel'
        if calfactor != 1:
            x_label = 'keV'
        for x in range(np.size(hist)):
            Xaxisfactor.append(x/calfactor)
        for x in range(np.size(peaklocations)):
            print(str(peaklocations[x]/calfactor) + ' ' + str(x_label) + ' | ' + str(hist[int(peaklocations[x])]) + ' counts | ' + str(FWHM[0][x]/calfactor) + ' ' + str(x_label) + ' FWHM | ')
            peaklocations2.append(peaklocations[x])
            allFWHM.append(FWHM[0][x]/calfactor)
            allheights.append(hist[int(peaklocations[x])])
        np_peaklocations2 = np.array(peaklocations2, dtype = int)
        averageFWHM = sum(allFWHM)/len(allFWHM)
        averageheight = sum(allheights)/len(allheights)
        print('Average height = ' + str(averageheight) + ' counts')
        print('Average FWHM = ' + str(averageFWHM) + ' ' + str(x_label) + '\n')
        plt.plot(Xaxisfactor, hist, label=filelocation)
        #plt.plot(np_peaklocations2/calfactor, hist[np_peaklocations2], "vk")
    except Exception as e:
        if filelocation == '':
            break
        else:
            print("Cannot load file," + str(e))

if calfactor == 1:
    plt.xlabel('Channel')
else:
    plt.xlabel('Energy in keV')
plt.ylabel('Counts')
plt.xlim(0)
plt.legend(loc='upper right')
plt.show()

