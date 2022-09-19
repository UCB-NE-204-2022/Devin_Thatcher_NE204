import h5py
import numpy as np

filelocation = input("Enter file location: ")
filelocation = filelocation.strip('"')
with h5py.File(filelocation, 'r') as f:
    data = np.array(f['raw_data'])
    spectra = []
    for a in range(np.size(data, 0)):
        inverteddata = []
        rowmax = np.amax(data[a])
        for b in range(np.size(data[a])):
            inverteddata.append(rowmax - data[a][b])
        pulseheight = np.sum(inverteddata)
        spectra.append(pulseheight)
    with open('spectradata.npy', 'wb') as f2:
        np.save(f2, np.array(spectra))
