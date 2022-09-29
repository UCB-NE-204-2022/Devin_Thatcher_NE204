import h5py
import numpy as np
import matplotlib.pyplot as plt

#adjust these values
rt = 150 #risetime
ft = 200 #flattop
dc = 10000 #decayconstant
pulsesToPlot = 1000
XRange = 3000

filelocation = input("Enter file location: ") #copy and paste file path
filelocation = filelocation.strip('"')
with h5py.File(filelocation, 'r') as f:
    data = np.array(f['raw_data'])
    pulses = np.empty([pulsesToPlot, XRange])
    for a in range(pulsesToPlot):
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
    for x in range(pulsesToPlot):
        plt.plot(pulses[x])

plt.show()
