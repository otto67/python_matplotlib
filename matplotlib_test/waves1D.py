from abc import abstractmethod
import numpy as np
import math
from numpy.core.function_base import linspace
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpmath as mpm

""" Class for animating simple 1-dimensional waves

    Raises:
        NotImplementedError: A subclass must implement the wave form
"""
class Wave():
    def __init__(self, npts=100, xmin=-1.0, xmax=2.0, dt=0.1):
        self.n_points = npts # Number of spatial points
        self.x_min = xmin 
        self.x_max = xmax
        self.dt = dt
        self.time = 0.0
        self.x = linspace(xmin, xmax, npts)
        self.y = np.zeros(npts)

    @abstractmethod
    def waveForm(self, x, t):
        """ Defines the amplitude of the wave at a given time and spatial point
        Args:
            x (float): Spatial point
            t (float): Time
        Raises:
            NotImplementedError: Must be implemented in a subclass
        """        
        raise NotImplementedError
    
    # initial wave form
    def initialize(self):
        for index, coor in enumerate(self.x):
            self.y[index] = self.waveForm(coor, 0)
        return self

    # update time and wave form
    def prepare4TimeStep(self):
        self.time += self.dt
        for index, coor in enumerate(self.x):
            self.y[index] = self.waveForm(coor, self.time)
 
class SolitonWave(Wave):
    def __init__(self, npts=100, xmin=-1, xmax=2.0, dt=0.01, c=0.1, beta=0.001):
        super().__init__(npts, xmin, xmax, dt)
        self.c = c          
        self.beta = beta 

    def waveForm(self, x, t):
        return 3.0*self.c*pow(mpm.sech((self.c/self.beta)**0.5 * (x - self.c*t)/2), 2)

class HarmonicWaveDispersive(Wave):
    def __init__(self, npts=100, xmin=-1, xmax=2.0, dt=0.01, a=[0.1, 0.1, 0.1], k=None):
        super().__init__(npts, xmin, xmax, dt)
        self.amp = a
               
        if k is None:
            self.k = []
            for i in range(len(a)):
                self.k.append(2*(i+1)*np.pi /(xmax - xmin)) # Let wavelength equal i times interval length
        else:
            self.k = k

    def omega(self, k):
        """Dispersion relation
        Args:
            k (float): Wave number
        Returns:
            float: Angular frequency
        """        
        return 1.0 + k/10

    def waveForm(self, x, t):
        retval = 0.0
        for index, wn in enumerate(self.k):
            retval += self.amp[index]*np.sin(wn*x - self.omega(wn)*t)
        return retval

class StandingWave(HarmonicWaveDispersive):
    def __init__(self, npts=100, xmin=-1, xmax=2.0, dt=0.01, a=[0.1], k=None):
        k = [8*np.pi /(xmax - xmin)]
        super().__init__(npts, xmin, xmax, dt, a, k)

    def waveForm(self, x, t):
        retval = 0.0
        for index, wn in enumerate(self.k):
            retval += self.amp[index]*(np.sin(wn*x - self.omega(wn)*t) + np.sin(wn*x + self.omega(wn)*t)) 
        return retval

class StandingWaveResonance(StandingWave):
    def __init__(self, npts=100, xmin=-1.0, xmax=2.0, dt=0.01):
        super().__init__(npts, xmin, xmax, dt)

    def waveForm(self, x, t):
        retval = super().waveForm(x, t)
        retval *= 0.01*t
        return retval