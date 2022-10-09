from cmath import pi
import math
import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(2)
x = np.linspace(-0.1,0.1,500)
y = 10**14/math.sqrt(4*pi*10*10**(-6))*math.e**(-x**2/(4*10*10**(-6))) + 10**5
ax1.plot(x, y, label='1 microsecond')
y = 10**14/math.sqrt(4*pi*10*10**(-6)*10)*math.e**(-x**2/(4*10*10**(-6)*10)) + 10**5
ax1.plot(x, y, label='10 microseconds')
ax1.legend()
ax1.set_title('Question 4.1\nThe hole concentration spreads out over time, but the center of the distribution stays in one place')
ax1.set_xlabel('Distance in cm')
ax1.set_ylabel('Hole concentration')

x = np.linspace(-0.1,0.1,500)
y = 10**14/math.sqrt(4*pi*10*10**(-6))*math.e**(-(x-0.005)**2/(4*10*10**(-6))) + 10**5
ax2.plot(x, y, label='1 microsecond')
y = 10**14/math.sqrt(4*pi*10*10**(-6)*10)*math.e**(-(x-0.05)**2/(4*10*10**(-6)*10)) + 10**5
ax2.plot(x, y, label='10 microseconds')
ax2.legend()
ax2.set_title('Question 4.2C\nThe hole concentration spreads out over time and the center of the distribution moves in the direction of the electric field')
ax2.set_xlabel('Distance in cm')
ax2.set_ylabel('Hole concentration')

plt.show()

