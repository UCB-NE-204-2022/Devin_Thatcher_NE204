import h5py
import numpy as np
import matplotlib.pyplot as plt

filelocation = input("Enter file location: ")
filelocation = filelocation.strip('"')
with h5py.File(filelocation, 'r') as f:
    data = np.array(f['raw_data'])
    data = data[:, :1000]
    arrayheight = np.size(data, 0)
    for x in range(arrayheight):
        plt.plot(data[x])

plt.show()
