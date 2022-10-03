import h5py
import numpy as np

XRange = 3000

filelocation = input("Enter file location: ")
filelocation = filelocation.strip('"')
with h5py.File(filelocation, 'r') as f:
    spectra = []
    for a in range(np.size(f['event_data'])):
        pulse = np.array(f['raw_data'][a, :XRange])
        baseline = np.average(pulse[:900])
        pulsemax = np.amax(pulse)
        pulsemin = np.average(baseline)
        pulseheight = pulsemax - pulsemin
        spectra.append(pulseheight)
    with open('spectradata.npy', 'wb') as f2:
        np.save(f2, np.array(spectra))
