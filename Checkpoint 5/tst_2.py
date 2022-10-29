import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(xlim=(0, 50), ylim=(-50, 50))


x = np.linspace(0, 50)
y= np.array((np.sin(x), np.cos(x)))



timeVals= np.empty((0,50))
tempVals= np.empty((2, 50))
line1, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2)




def animate(i):
    np.append(timeVals, x[i])
    for k in range(2):
        np.append(tempVals[k], y[k][i])
    line1.set_data(x, tempVals[0])
    line2.set_data(x, tempVals[1])

    return line1, line2


anim = animation.FuncAnimation(fig, animate,frames=50, interval=1000, blit=True)

plt.show()

