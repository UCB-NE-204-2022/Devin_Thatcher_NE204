from cmath import pi
import math
import matplotlib.pyplot as plt
import numpy as np

time = int(input('Time in microseconds: '))*10**(-6)
x = np.linspace(-0.1,0.1,100)
y = 10**14/math.sqrt(4*pi*10)*math.e**(-x**2/(4*10*time)) + 10**5

plt.plot(x, y)
plt.show()
