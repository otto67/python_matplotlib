import numpy as np
from numpy.core.function_base import linspace
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Base class that animates an object with an initial velocity being pulled down by gravity
# y(0) = 0, y'(0) = initial velocity (iv)
class GravField():
    def __init__(self, xmin=0.0, xmax=100.0, dx=0.5, iv=10, plot=True):
        """
        Constructor
        :param xmin: initial position x
        :param xmax: end position x
        :param dx: step along x-axis
        :param iv: initial velocity
        """
        npts = int((xmax - xmin) / dx)
        self.iv = iv # initial velocity
        self.theta = np.pi/6
        self.dx = dx
        self.npts = npts
        self.xmin = xmin
        self.xmax = xmax

        self.x = linspace(self.xmin, self.xmax, npts)
        self.sol = np.zeros(self.npts)
        self.sol += -9.81 * self.x * self.x / (2 * self.iv * self.iv * np.cos(self.theta) * np.cos(self.theta))
        self.sol += self.iv * np.tan(self.theta) * self.x

        if plot is True:
            self.createPlot()

        self.createAnimation()

    def animate(self, i):
        time = [self.x[i]]
        pos = [self.sol[i]]
        self.line.set_data(time, pos)
        return self.line,

    def createAnimation(self):
        fig, ax = plt.subplots()

        ax.plot(self.x, self.sol, linestyle='solid', linewidth='1')
        ax.set_xlabel('x')
        ax.set_ylabel('y(x)')
        ax.set_title(self.__class__)
        top = np.amax(self.sol)
        bottom = np.amin(self.sol)
        ax.set_xlim(self.xmin, self.xmax)
        ax.set_ylim(bottom, top)
        time = [self.x[0]]
        pos = [self.sol[0]]
        self.line, = ax.plot(time, pos, 'o', markersize=12)

        nframes = int((self.xmax - self.xmin)/self.dx)

        ani = animation.FuncAnimation(fig, self.animate, frames=nframes,  blit=True, interval=1)
        plt.show()

    def createPlot(self):

        font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
        font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}

        plt.subplot(1, 2, 1)
        plt.plot(self.x, self.sol, linestyle='solid', linewidth='1')
        plt.title("Plot", fontdict=font2, loc='center')
        plt.xlabel("Time", fontdict=font2)
        plt.ylabel("Position", fontdict=font2)
        plt.grid(axis='y', color='green', linestyle='--', linewidth=0.5)

        plt.subplot(1, 2, 2)
        plt.scatter(self.x, self.sol, s=0.01)
        plt.title("Scatter", fontdict=font2)

        plt.suptitle("Simulation", fontdict=font1)
        plt.subplots_adjust(wspace=0, hspace=0., top=0.99, bottom=0.01,
                            left=0.01, right=0.99)
        plt.show()

