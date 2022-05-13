import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from math import sin, cos, tau

kwargs = input()
states = int(input())
if kwargs[1] == 'x':
    point = float(input())

"""
First kwarg determines if the wavefunction should be (f)illed.
Second kwarg chooses between wavefunction (w) and probability density (p).
Third kwarg enables plotting of the (c)omponents.
Fourth kwarg enables (n)ormalization or chooses not to (u).
Fifth kwarg chooses whether to display a superposition of (a)ll states or any (s)ingle eigenstates.
States determine which state to show, or until which state to superimpose.
"""

# No. of elements at which we compute the wavefunctions.
ele = 1000
l = 10

# Initializing the 3-dimensional graph.
if kwargs[1] == 'w':
    ax = plt.axes(projection = '3d')

# Initializing the x-axis and the eigenfunctions.
x = np.linspace(0, l, ele)
ex = np.linspace(-.25, l+.25, ele)
zero = np.zeros(ele)

# Initializing a time-space.
time = np.linspace(0, tau, ele)

for t in time:
    # Computing the wavefunction from the various eigenfunctions of the system.
    psi_unnorm = zero
    if kwargs[4] == 'a':
        for i in range(1, states + 1):
            psi_unnorm = psi_unnorm + ((2/l)**.5) * np.sin(i*tau*x/(2*l)) * np.exp(i**2 * 1j*t)
    elif kwargs[4] == 's':
        psi_unnorm = ((2/l)**.5) * np.sin(states*tau*x/(2*l)) * np.exp(states**2 * 1j*t)

    psiunnormpsi = np.square(np.absolute(psi_unnorm))

    if kwargs[3] == 'n':
        psi = psi_unnorm / (np.sum(psiunnormpsi))**.5
        psistarpsi = np.square(np.absolute(psi))
    else:
        psi = psi_unnorm
        psistarpsi = psiunnormpsi

    # Setting the axes limits and labels.
    if kwargs[1] == 'w':
        ax.set_xlim(-.25, l+.25)
        ax.set_ylim(-1.25, 1.25)
        ax.set_zlim(-1.25, 1.25)
        ax.set_xlabel("Box")
        ax.set_ylabel("Imaginary Component")
        ax.set_zlabel("Real Component")
        ax.plot3D(ex, zero, zero, 'k')
        ax.plot3D(x, np.imag(psi), np.real(psi), 'b')

    if kwargs[1] == 'x':
        pnt = int(point * ele)
        plt.xlim(-1, 1)
        plt.ylim(-1, 1)
        plt.xlabel('Real Component')
        plt.ylabel('Imaginary Component')
        plt.grid()
        plt.quiver([0, 0], np.real(psi[pnt]), np.imag(psi[pnt]))

    # Plotting the box, wavefunction and its components.
    if kwargs[0] == 'f':
        for m in range(0, 100, 1):
            n = m/100
            ax.plot3D(x, n*np.imag(psi), n*np.real(psi), 'c')
    if kwargs[2] == 'c':
        ax.plot3D(x, np.imag(psi), zero)
        ax.plot3D(x, zero, np.real(psi))

    # Drawing the plot.
    plt.draw()
    if kwargs[1] == 'p':
        plt.xlim(-.25, l+.25)
        plt.ylim(0, 0.225)
        plt.xlabel('Box')
        plt.ylabel('Probability Density')
        plt.plot(x, psistarpsi)
    plt.pause(0.00001)
    plt.cla()
