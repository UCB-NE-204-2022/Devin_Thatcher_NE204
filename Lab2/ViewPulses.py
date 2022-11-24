import h5py
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

events = 10
XRange = 2000
pulselength = 250
preTrgrDly = 1000

def func(x, a, c, d):
    return a*np.exp(-c*x)+d

filelocation = input("Copy & paste .h5 file path: ")
filelocation = filelocation.strip('"')
with h5py.File(filelocation, 'r') as f:
    for a in range(0, events):
        try:
            pulse = np.array(f['raw_data'][a, :XRange])  # type: ignore
            baseline = np.average(pulse[:preTrgrDly-100])
            bpulse = []
            for b in range(XRange):
                bpulse.append(pulse[b]-baseline)
            decay = bpulse[preTrgrDly:preTrgrDly+pulselength]
            x = np.linspace(preTrgrDly, preTrgrDly+pulselength, pulselength)
            popt, pcov = curve_fit(func, x, decay, [200, 0.001, 0])
            plt.plot(bpulse)
            plt.plot(x, func(x, *popt))
            print(popt)
        except:
            pass

plt.show()
