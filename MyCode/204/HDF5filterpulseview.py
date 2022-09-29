import h5py
import numpy as np
import matplotlib.pyplot as plt

#adjust these values
risetime = 150
flattop = 200
decayconstant = 10000
numbertoplot = 1000
plotxrange = 6000

filelocation = input("Enter file location: ") #copy file path and paste
filelocation = filelocation.strip('"')
with h5py.File(filelocation, 'r') as f:
    data = np.array(f['raw_data'])
    pulses = np.empty([numbertoplot, plotxrange])
    for a in range(numbertoplot):
        pulse = data[a, :plotxrange]
        size = np.size(pulse)
        baseline = np.average(data[a, :900])
        bpulse = []
        cpulse = []
        dpulse = [0]
        for b in range(size): #take baseline average to be 0
            bpulse.append(pulse[b] - baseline) 
        for b in range(size): #filter values
            if b < risetime:
                cpulse.append(bpulse[b])
            elif risetime <= b <= risetime+flattop-1:
                cpulse.append(bpulse[b]-bpulse[b-risetime])
            elif risetime+flattop <= b <= 2*risetime+flattop-1:
                cpulse.append(bpulse[b]-bpulse[b-risetime]-bpulse[b-(risetime+flattop)])
            else:
                cpulse.append(bpulse[b]-bpulse[b-risetime]-bpulse[b-(risetime+flattop)]+bpulse[b-(2*risetime+flattop)])
        for b in range(1, size): #integrate filtered values (with pole zero correction)
            dpulse.append(dpulse[b-1]*(1+1/decayconstant)+cpulse[b])
        pulses[a]=np.array(dpulse)
    for x in range(0,numbertoplot):
        plt.plot(pulses[x])

plt.show()
