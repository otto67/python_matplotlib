import numpy as np
from numpy.core.function_base import linspace
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.integrate as igr
from scipy.integrate import odeint, solve_ivp

class FreeFall():
    def __init__(self, dt=0.01, U0=100, alpha = 0.0001, beta=0.0001):
        self.dt = dt
        self.alpha = alpha
        self.beta = beta
        self.U0 = U0

    def eqSys(self, t, state, alpha, beta):
        x, y, u, v = state
        dx = u
        dy = v
        du = -beta * u*u
        dv = -(alpha*v*v + 9.81)
        return [dx, dy, du, dv]

    def setIC(self):
        return [0.0, 0.0, self.U0*np.cos(np.pi/6), self.U0*np.sin(np.pi/6)]

    def solve(self):
        y0 = self.setIC()
        p = (self.alpha, self.beta)  # Parameters of the system

        # Needed for the ivp function
        t_span = (0.0, 40.0)
        t = np.arange(0.0, 40.0, 0.001)

        result_odeint = odeint(self.eqSys, y0, t, p, tfirst=True)
        result_solve_ivp = solve_ivp(self.eqSys, t_span, y0,  args=p, method='LSODA', t_eval=t)
        self.plot(t, result_solve_ivp)

    def plot(self, t, result):
        fig = plt.figure()
        ax = fig.add_subplot(1, 4, 1)
        ax.plot(t, result.y[0,:])
        ax.set_title("x position")

        ax = fig.add_subplot(1, 4, 2)
        ax.plot(t, result.y[1, :])
        ax.set_title("y position")

        ax = fig.add_subplot(1, 4, 3)
        # ax.plot(t, result_odeint[:, 2])

        ax.plot(t, result.y[2, :])
        ax.set_title("x velocity")

        ax = fig.add_subplot(1, 4, 4)
        # ax.plot(t, result_odeint[:, 1])
        ax.plot(t, result.y[3, :])
        ax.set_title("y velocity")

        fig.set_size_inches(15.5, 10.5)
        plt.show()