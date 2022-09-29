import h5py
import numpy as np

#adjust these values
rt = 150 #risetime
ft = 200 #flattop
dc = 10000 #decayconstant
XRange = 2000

filelocation = input("Enter file location: ") #copy and paste file path
filelocation = filelocation.strip('"')
with h5py.File(filelocation, 'r') as f:
    spectra = []
    data = np.array(f['raw_data'])
    pulses = np.empty([np.size(data, 0), XRange])
    for a in range(np.size(data, 0)):
        pulse = data[a, :XRange]
        size = np.size(pulse)
        baseline = np.average(pulse[:900])
        bpulse = []
        cpulse = []
        dpulse = [0]
        for b in range(size): #take baseline average to be 0
            bpulse.append(pulse[b] - baseline) 
        for b in range(size): #filter values
            if b < rt:
                cpulse.append(bpulse[b])
            elif rt <= b <= rt+ft-1:
                cpulse.append(bpulse[b]-bpulse[b-rt])
            elif rt+ft <= b <= 2*rt+ft-1:
                cpulse.append(bpulse[b]-bpulse[b-rt]-bpulse[b-(rt+ft)])
            else:
                cpulse.append(bpulse[b]-bpulse[b-rt]-bpulse[b-(rt+ft)]+bpulse[b-(2*rt+ft)])
        for b in range(1, size): #integrate filtered values (with pole zero correction)
            dpulse.append(dpulse[b-1]*(1+1/dc)+cpulse[b])
        pulses[a]=np.array(dpulse)
        pulseheight = np.amax(pulses[a])
        spectra.append(pulseheight)
    with open('spectradata2.npy', 'wb') as f2:
        np.save(f2, np.array(spectra))
