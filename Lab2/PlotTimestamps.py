import h5py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filelocation = input("Copy & paste .h5 file path: ")
filelocation = filelocation.strip('"')
with h5py.File(filelocation, 'r') as f:
    data = np.array(f['event_data'])
    eventdata = pd.DataFrame(data)
    eventtime = eventdata['timestamp']/250000000
    eventtime.plot()
    plt.xlabel('Event #')
    plt.ylabel('Time passed in seconds')
    plt.show()