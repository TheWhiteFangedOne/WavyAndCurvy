import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import animation
from math import sin, cos, tau

# No. of elements at which we compute the wavefunctions.
ele = 1000
l = 10

kwargs = input()
states = int(input())
positi = int(float(input())*ele)

"""
First kwarg determines if the wavefunction should be (f)illed.
Second kwarg chooses between wavefunction (w) and probability density (p).
Third kwarg enables plotting of the (c)omponents.
Fourth kwarg enables (n)ormalization or chooses not to (u).
Fifth kwarg chooses whether to display a superposition of (a)ll states or any (s)ingle eigenstates.
States determine which state to show, or until which state to superimpose.
"""

if kwargs[3] == 'n':
    norm = states**-2
    norm_p = norm**2
else:
    norm = 1

# Initializing the x-axis and the eigenfunctions.
x = np.linspace(0, l, ele)
ex = np.linspace(-.25, l+.25, ele)
zero = np.zeros(ele)

# Initializing the plot
fig = plt.figure()
ax = fig.add_subplot(1, 2, 1, projection = '3d')
ax.set_xlim(-.25, l+.25)
ax.set_ylim(-1.25*norm, 1.25*norm)
ax.set_zlim(-1.25*norm, 1.25*norm)
ax.set_xlabel("Box")
ax.set_ylabel("Imaginary Component")
ax.set_zlabel("Real Component")
ax.plot3D(ex, zero, zero, 'k')
line, = ax.plot3D([], [], [])

ay = fig.add_subplot(2, 2, 2)
ay.set_xlim(-.25, l+.25)
ay.set_ylim(0, norm_p)
ay.set_xlabel("Box")
ay.set_ylabel("Probability Density")
prob, = ay.plot([], [])

az = fig.add_subplot(2, 2, 4)
az.set_xlim(-1.25*norm, 1.25*norm)
az.set_ylim(-1.25*norm, 1.25*norm)
az.set_xlabel("Real Component")
az.set_ylabel("Imaginary Component")
az.set_aspect(1)
wave, = ax.plot([], [])

step = [line, prob, wave]

def animate(t):
    t = t*tau/1000
    psi_unnorm = zero
    for i in range(0, states + 1):
        psi_unnorm = psi_unnorm + ((2/l)**.5) * np.sin(i*tau*x/(2*l)) * np.exp(i**2 * 1j*t)
    psiunnormpsi = np.square(np.absolute(psi_unnorm))

    if kwargs[3] == 'n':
        psi = psi_unnorm / (np.sum(psiunnormpsi))**.5
        psistarpsi = np.square(np.absolute(psi))
    else:
        psi = psi_unnorm
        psistarpsi = psiunnormpsi

    wave.set_data(np.real(psi)[positi], np.imag(psi)[positi])
    prob.set_data(x, psistarpsi)
    line.set_data(x, np.imag(psi))
    line.set_3d_properties(np.real(psi))
    return step

anim = animation.FuncAnimation(fig, animate, frames = 1000, interval = 20, blit=True)
plt.show()
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
