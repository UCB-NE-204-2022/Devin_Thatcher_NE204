import h5py
import numpy as np
import matplotlib.pyplot as plt

risetime = 150
flattop = 200
numbertoplot = 1000

filelocation = input("Enter file location: ")
filelocation = filelocation.strip('"')
with h5py.File(filelocation, 'r') as f:
    data = np.array(f['raw_data'])
    pulses = np.empty([numbertoplot, 3000])
    for a in range(numbertoplot):
        pulse = data[a, :3000]
        size = np.size(pulse)
        baseline = np.average(data[a, :900])
        bpulse = []
        cpulse = []
        dpulse = [0]
        for b in range(size):                       
            bpulse.append(pulse[b] - baseline)
        for b in range(size):
            if b < risetime:
                cpulse.append(bpulse[b])
            elif risetime <= b <= risetime+flattop-1:
                cpulse.append(bpulse[b]-bpulse[b-risetime])
            elif risetime+flattop <= b <= 2*risetime+flattop-1:
                cpulse.append(bpulse[b]-bpulse[b-risetime]-bpulse[b-(risetime+flattop)])
            else:
                cpulse.append(bpulse[b]-bpulse[b-risetime]-bpulse[b-(risetime+flattop)]+bpulse[b-(2*risetime+flattop)])
        for b in range(1, size):
            dpulse.append(dpulse[b-1]+cpulse[b])
        pulses[a]=np.array(dpulse)
    for x in range(0,numbertoplot):
        plt.plot(pulses[x])

plt.show()
