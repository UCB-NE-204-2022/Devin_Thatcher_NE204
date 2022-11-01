import h5py
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#adjust these values
rt = 50 #risetime
ft = 30 #flattop
preTrgrDly = 1000
XRange = 1500
events = 500
dc = 150

def func(x, a, c, d):
    return a*np.exp(-c*x)+d

filelocation = input("Copy & paste .h5 file path: ")
filelocation = filelocation.strip('"')
with h5py.File(filelocation, 'r') as f:
    pulses = np.empty([events, 2*rt+ft+100])
    for a in range(events):
        try:
            pulse = np.array(f['raw_data'][a, :XRange])
            baseline = np.average(pulse[:int(preTrgrDly//1.5)])
            bpulse = []
            cpulse = []
            dpulse = [0]
            for b in range(XRange):
                bpulse.append(pulse[b]-baseline)
            decay = bpulse[preTrgrDly+20:XRange]
            x = np.linspace(preTrgrDly+20, XRange, XRange-(preTrgrDly+20))
            popt, pcov = curve_fit(func, x, decay, [200, 0.001, 100])
            if 0<popt[0] and 0<popt[1] and 0<popt[2]:
                for b in range(int(preTrgrDly-100), int(preTrgrDly+2*rt+ft)):
                    if b < rt:
                        cpulse.append(bpulse[b])
                    elif rt <= b <= rt+ft-1:
                        cpulse.append(bpulse[b]-bpulse[b-rt])
                    elif rt+ft <= b <= 2*rt+ft-1:
                        cpulse.append(bpulse[b]-bpulse[b-rt]-bpulse[b-(rt+ft)])
                    else:
                        cpulse.append(bpulse[b]-bpulse[b-rt]-bpulse[b-(rt+ft)]+bpulse[b-(2*rt+ft)])
                for b in range(1, int(2*rt+ft+100)):
                    dpulse.append(dpulse[b-1]*(1+1/dc)+cpulse[b])
                pulses[a]=np.array(dpulse)
        except:
            pass
    for x in range(events):
        plt.plot(pulses[x])

plt.show()
