import h5py
import numpy as np
from scipy.optimize import curve_fit

#adjust these values
rt = 350 #risetime
ft = 200 #flattop
preTrgrDly = 1000
XRange = 10000

def func(x, a, c, d):
    return a*np.exp(-c*x)+d

filelocation = input("Copy & paste .h5 file path: ")
filelocation = filelocation.strip('"')
with h5py.File(filelocation, 'r') as f:
    useablefraction = 0
    spectra = []
    for a in range(120000):
        try:
            pulse = np.array(f['raw_data'][a, :XRange])
            baseline = np.average(pulse[:int(preTrgrDly//1.5)])
            bpulse = []
            cpulse = []
            dpulse = [0]
            for b in range(XRange):
                bpulse.append(pulse[b] - baseline)
            decay = bpulse[preTrgrDly+100:XRange]
            x = np.linspace(preTrgrDly+100, XRange, XRange-(preTrgrDly+100))
            popt, pcov = curve_fit(func, x, decay, [200, 0.0001, 0])
            if 0 < popt[0] and 0 < popt[1] and 0 < popt[2]:
                for b in range(int(preTrgrDly+2*rt+ft)):        
                    if b < rt:
                        cpulse.append(bpulse[b])
                    elif rt <= b <= rt+ft-1:
                        cpulse.append(bpulse[b]-bpulse[b-rt])
                    elif rt+ft <= b <= 2*rt+ft-1:
                        cpulse.append(bpulse[b]-bpulse[b-rt]-bpulse[b-(rt+ft)])
                    else:
                        cpulse.append(bpulse[b]-bpulse[b-rt]-bpulse[b-(rt+ft)]+bpulse[b-(2*rt+ft)])
                for b in range(1, int(preTrgrDly+2*rt+ft)):
                    dpulse.append(dpulse[b-1]*(1+popt[1])+cpulse[b])
                spectra.append(np.average(dpulse[preTrgrDly+rt+50:preTrgrDly+rt+ft-50]))
                useablefraction += 1
                print(useablefraction)
        except:
            pass
    spectraname = input("Enter name of .npy file to save spectra: ")
    with open(spectraname + '.npy', 'wb') as f2:
        np.save(f2, np.array(spectra))
