import h5py
import numpy as np

XRange = 1800
preTrgrDly = 1000

filelocation = input("Copy & paste .h5 file path: ")
filelocation = filelocation.strip('"')
with h5py.File(filelocation, 'r') as f:
    spectra = []
    for a in range(np.size(f['event_data'])):
        pulse = np.array(f['raw_data'][a, :XRange])
        baseline = np.average(pulse[:int(preTrgrDly//1.5)])
        pulsemax = np.amax(pulse)
        pulsemin = np.average(baseline)
        pulseheight = pulsemax - pulsemin
        spectra.append(pulseheight)
    spectraname = input("Enter name of .npy file to save spectra: ")
    with open(spectraname + '.npy', 'wb') as f2:
        np.save(f2, np.array(spectra))
