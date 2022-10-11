import h5py
import numpy as np
import matplotlib.pyplot as plt

pulsesToPlot = 100
XRange = 1800

filelocation = input("Copy & paste .h5 file path: ")
filelocation = filelocation.strip('"')
with h5py.File(filelocation, 'r') as f:
    for a in range(0, pulsesToPlot):
        pulse = np.array(f['raw_data'][a, :XRange])
        plt.plot(pulse)

plt.show()
