import numpy as np
import matplotlib.pyplot as plt

counts = []

filelocation = input("File Location:")
filelocation = filelocation.strip('"')

with open(filelocation) as MCAfile:
    line = MCAfile.readline()
    while line != '':
        try:
            y = int(line)
            counts.append(y)
            line = MCAfile.readline()
        except ValueError:
            line = MCAfile.readline()

plt.figure(1)
plt.subplot(211)
plt.plot(counts)
plt.xlabel('Channel')
plt.ylabel('Counts')
plt.subplot(212)
plt.plot(counts)
plt.xlabel('Channel')
plt.ylabel('Counts')
plt.yscale('log')

plt.show()