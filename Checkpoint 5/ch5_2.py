import time
import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from DAH import DS18B20

fig = plt.figure()
ax = plt.axes(xlim=(0, 50), ylim=(-50, 50))
line, = ax.plot([], [], lw=2)

x = np.linspace(0, 50)
y= np.sin(x)
temp0= DS18B20(address= '10-000080265b6d6')

timeVals=[]
tempVals=[]
init_time= time.time()

def init():
    line.set_data([], [])
    return line,

def animate(i):
    timeVals.append(time.time() - init_time)
    tempVals.append(temp0.getCelsius())
    line.set_data(timeVals,tempVals)
    return line,


anim = animation.FuncAnimation(fig, animate, init_func=init, frames=50, interval=1000, blit=True)

plt.show()


