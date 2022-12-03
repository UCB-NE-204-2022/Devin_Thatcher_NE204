import h5py
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#adjust these values
rt = 500 #risetime
preTrgrDly = 1000
XRange = 2000
events = 500

filelocation = input("Copy & paste .h5 file path: ")
filelocation = filelocation.strip('"')
with h5py.File(filelocation, 'r') as f:
    pulses = np.empty([events, rt+1])
    for a in range(events):
        pulse = np.array(f['raw_data'][a, :XRange])  # type: ignore
        baseline = np.average(pulse[:int(preTrgrDly//1.5)])
        bpulse = []
        cpulse = [0]
        for b in range(XRange):
            bpulse.append(pulse[b]-baseline)
        for b in range(rt):
            cpulse.append(cpulse[b]+bpulse[b+preTrgrDly])
        pulses[a]=np.array(cpulse)
    for x in range(events):
        plt.plot(pulses[x])

plt.show()
