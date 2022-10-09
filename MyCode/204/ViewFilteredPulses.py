import h5py
import numpy as np
import matplotlib.pyplot as plt

#adjust these values
rt = 150 #risetime
ft = 200 #flattop
dc = 10000 #decayconstant
pulsesToPlot = 200
XRange = 3000
preTrgrDly = 1000

filelocation = input("Enter .h5 file location: ") #copy and paste file path
filelocation = filelocation.strip('"')
with h5py.File(filelocation, 'r') as f:
    pulses = np.empty([pulsesToPlot, XRange])
    for a in range(pulsesToPlot):
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
        pulses[a]=np.array(dpulse)
    for x in range(pulsesToPlot):
        plt.plot(pulses[x])

plt.show()
