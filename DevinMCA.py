import numpy as np
from matplotlib import pyplot as plt

channel = []
counts = []
x = 1

filelocation = input("File Location:")
filelocation = filelocation.strip('"')

with open(filelocation) as MCAfile:
    line = MCAfile.readline()
    while line != '':
        try:
            y = int(line)
            counts.append(y)
            channel.append(x)
            x += 1
            line = MCAfile.readline()
        except ValueError:
            line = MCAfile.readline()

print(channel)
print(counts)
