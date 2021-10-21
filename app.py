import numpy as np
from numpy.core.function_base import linspace
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from matplotlib_test import waves1D as wd
from matplotlib_test import animator as anim
from matplotlib_test import gravity

if __name__ == "__main__":

    myFDM = gravity.GravField(plot=False)

    simlist = []
    simlist.append(wd.StandingWaveResonance().initialize())
    simlist.append(wd.StandingWave().initialize())
    simlist.append(wd.SolitonWave().initialize())
    simlist.append(wd.HarmonicWaveDispersive().initialize())
    anim.WaveAnimator(simlist).createAnimation()
