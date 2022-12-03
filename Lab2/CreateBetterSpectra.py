import h5py
import numpy as np

#adjust these values
rt = 300 #risetime
preTrgrDly = 1000
XRange = 2000
events = 400000

filelocation = input("Copy & paste .h5 file path: ")
filelocation = filelocation.strip('"')
with h5py.File(filelocation, 'r') as f:
    spectra = []
    for a in range(events):
        pulse = np.array(f['raw_data'][a, :XRange])  # type: ignore
        baseline = np.average(pulse[:int(preTrgrDly//1.5)])
        pulse = pulse - baseline
        spectra.append(np.sum(pulse[preTrgrDly:preTrgrDly+rt])/rt)
    spectraname = input("Enter name of .npy file to save spectra: ")
    with open(spectraname + '.npy', 'wb') as f2:
        np.save(f2, np.array(spectra))
