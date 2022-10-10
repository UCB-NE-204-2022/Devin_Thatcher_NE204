import h5py
import numpy as np

#adjust these values
rt = 150 #risetime
ft = 200 #flattop
dc = 10000 #decayconstant
XRange = 3000
preTrgrDly = 1000

filelocation = input("Copy & paste .h5 file path: ")
filelocation = filelocation.strip('"')
with h5py.File(filelocation, 'r') as f:
    spectra = []
    for a in range(np.size(f['event_data'])):
        pulse = np.array(f['raw_data'][a, :XRange])
        baseline = np.average(pulse[:int(preTrgrDly//1.5)])
        bpulse = []
        cpulse = []
        dpulse = [0]
        for b in range(XRange):
            bpulse.append(pulse[b] - baseline) 
            if b < rt:
                cpulse.append(bpulse[b])
            elif rt <= b <= rt+ft-1:
                cpulse.append(bpulse[b]-bpulse[b-rt])
            elif rt+ft <= b <= 2*rt+ft-1:
                cpulse.append(bpulse[b]-bpulse[b-rt]-bpulse[b-(rt+ft)])
            else:
                cpulse.append(bpulse[b]-bpulse[b-rt]-bpulse[b-(rt+ft)]+bpulse[b-(2*rt+ft)])
        for b in range(1, XRange):
            dpulse.append(dpulse[b-1]*(1+1/dc)+cpulse[b])
        spectra.append(np.amax(dpulse))
    spectraname = input("Enter name of .npy file to save spectra: ")
    with open(spectraname + '.npy', 'wb') as f2:
        np.save(f2, np.array(spectra))
