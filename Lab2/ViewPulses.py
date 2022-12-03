import h5py
import numpy as np
import matplotlib.pyplot as plt

events = 500
XRange = 2000
preTrgrDly = 1000

filelocation = input("Copy & paste .h5 file path: ")
filelocation = filelocation.strip('"')
with h5py.File(filelocation, 'r') as f:
    for a in range(0, events):
        pulse = np.array(f['raw_data'][a, :XRange])  # type: ignore
        baseline = np.average(pulse[:preTrgrDly-100])
        pulse = pulse - baseline
        plt.plot(pulse)

plt.show()
