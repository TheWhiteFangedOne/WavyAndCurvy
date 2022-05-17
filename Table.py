import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import animation
from matplotlib import cm
from math import sin, cos, tau

ele = 1000
a = 9
b = 16

norm = 1

mode = input()
n = int(input())
m = int(input())

x = np.linspace(0, a, ele)
y = np.linspace(0, b, ele)
xx, yy = np.meshgrid(x, y)
zero = np.zeros(ele)

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.set_xlim(0, a)
ax.set_ylim(0, b)
ax.set_zlim(-norm, norm)

psi = np.sin(n*xx*tau/(2*a)) * np.sin(m*yy*tau/(2*b))

if mode == 'anim':
    wavefunc = ax.plot_surface(xx, yy, psi, cmap = cm.inferno, linewidth=0)

    def TimeEvo(t):
        t = t*tau/1000
        psi = (np.sin(n*xx*tau/(2*a)) * cos(t)) * (np.sin(m*yy*tau/(2*b)) * cos(t))

        ax.set_xlim(0, a)
        ax.set_ylim(0, b)
        ax.set_zlim(-norm, norm)

        ax.clear()
        wavefunc = ax.plot_surface(xx, yy, psi, cmap = cm.inferno, linewidth=0)
        return wavefunc

    anim = animation.FuncAnimation(fig, TimeEvo, frames = 1000, interval = 20, blit=False)
else:
    ax.plot_surface(xx, yy, psi, cmap = cm.inferno, linewidth=0)

plt.show()
