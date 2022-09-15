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

filelocation = 1
unstackedData = []

while True:
    filelocation = input("File Location:")
    filelocation = filelocation.strip('"')
    try:
        counts = np.array(getData(filelocation))
        unstackedData.append(counts)
    except:
        break

stackedData = np.vstack(unstackedData)
arrayheight = np.size(stackedData, 0)

plt.figure(1)
plt.subplot(211)
for x in range(arrayheight):
     plt.plot(stackedData[x])
plt.xlabel('Channel')
plt.ylabel('Counts')
plt.subplot(212)
for x in range(arrayheight):
     plt.plot(stackedData[x])
plt.xlabel('Channel')
plt.ylabel('Counts')
plt.yscale('log')

plt.show()