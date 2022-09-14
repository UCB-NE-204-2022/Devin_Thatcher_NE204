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

plt.plot(counts)
plt.show()