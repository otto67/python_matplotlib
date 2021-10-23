from matplotlib_test import waves1D as wd
from matplotlib_test import animator as anim
from matplotlib_test import gravity
from scipy_test import integrate
from scipy_test import odesolver

if __name__ == "__main__":

    integrate.integrate(2, 1, 1)

    sim = odesolver.FreeFall()
    sim.solve()

    myFDM = gravity.GravField(plot=False)

    simlist = []
    simlist.append(wd.StandingWaveResonance().initialize())
    simlist.append(wd.StandingWave().initialize())
    simlist.append(wd.SolitonWave().initialize())
    simlist.append(wd.HarmonicWaveDispersive().initialize())
    anim.WaveAnimator(simlist).createAnimation()
