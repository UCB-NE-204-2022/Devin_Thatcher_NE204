import h5py
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

pulsesToPlot = 500
XRange = 2000

def func(x, a, c, d):
    return a*np.exp(-c*x)+d

filelocation = input("Copy & paste .h5 file path: ")
filelocation = filelocation.strip('"')
with h5py.File(filelocation, 'r') as f:
    for a in range(0, pulsesToPlot):
        try:
            pulse = np.array(f['raw_data'][a, :XRange])
            baseline = np.average(pulse[:800])
            bpulse = []
            for b in range(XRange):
                bpulse.append(pulse[b]-baseline)
            decay = bpulse[1020:XRange]
            x = np.linspace(1020, XRange, XRange-1020)
            popt, pcov = curve_fit(func, x, decay, [200, 0.001, 100])
            plt.plot(bpulse)
            plt.plot(x, func(x, *popt))
        except:
            pass

plt.show()
