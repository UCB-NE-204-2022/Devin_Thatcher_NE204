import h5py
import numpy as np
import matplotlib.pyplot as plt

pulsesToPlot = 100
XRange = 3000

filelocation = input("Enter .h5 file location: ")
filelocation = filelocation.strip('"')
with h5py.File(filelocation, 'r') as f:
    for a in range(0, pulsesToPlot):
        pulse = np.array(f['raw_data'][a, :XRange])
        plt.plot(pulse)

plt.show()
