import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(xlim=(0, 50), ylim=(-50, 50))
line, = ax.plot([], [], lw=2)

x = np.linspace(0, 50)
y= np.sin(x) 
t=0

timeVals=[]
tempVals=[]

def init():
    line.set_data([], [])
    return line,

def animate(i):
    timeVals.append(x[i])
    tempVals.append(y[i])
    line.set_data(timeVals,tempVals)
    return line,


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=50, interval=100, blit=True)

plt.show()

