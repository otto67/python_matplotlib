import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from . import waves1D

class WaveAnimator():

    def __init__(self, waves):
        self.wavelist = waves


    def animate(self, i):
        self.wavelist[self.simno].prepare4TimeStep()
        self.line.set_ydata(self.wavelist[self.simno].y)
        return self.line, 

    def createAnimation(self):
        for i, wave in enumerate(self.wavelist):
            fig, ax = plt.subplots()
            self.simno = i
            self.line, = ax.plot(wave.x, wave.y)
            ax.set_xlabel('t')
            ax.set_ylabel('y(t)')
            ax.set_title(wave.__class__)

            ani = animation.FuncAnimation(fig, self.animate, frames=20,  blit=True, interval=10)
            plt.show()