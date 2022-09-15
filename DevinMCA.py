import numpy as np
import matplotlib.pyplot as plt

def getData(x):
    counts = []
    with open(x) as MCAfile:
        line = MCAfile.readline()
        while line != '':
            try:
                counts.append(int(line))
                line = MCAfile.readline()
            except:
                line = MCAfile.readline()
    return counts

file = []
unstackedData = []

while True:
    filelocation = input("Enter file locations then 'done' to plot: ")
    filelocation = filelocation.strip('"')
    try:
        counts = np.array(getData(filelocation))
        unstackedData.append(counts)
        file.append(filelocation)
    except:
        if filelocation == 'done':
            break
        else:
            print("Unable to load data")

stackedData = np.vstack(unstackedData)
arrayheight = np.size(stackedData, 0)

plt.title('MCA Data')
plt.figure(1)
plt.subplot(211)
for x in range(arrayheight):
     plt.plot(stackedData[x], label = file[x])
plt.xlabel('Channel')
plt.ylabel('Counts')
plt.legend()
plt.subplot(212)
for x in range(arrayheight):
     plt.plot(stackedData[x], label = file[x])
plt.xlabel('Channel')
plt.ylabel('Counts')
plt.yscale('log')

plt.show()