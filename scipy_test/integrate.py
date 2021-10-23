import numpy as np
from numpy.core.function_base import linspace
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.integrate as igr
from scipy.integrate import odeint, solve_ivp

# A simple function that integrates over an ellipse and an ellipsoid
# to find their area and volume. Also plots the ellipse and ellipsoid
def integrate(r=3.0, minor=2.0, minor2=1.0):

    f = lambda x: x
    g = lambda x, y: 1
    h = lambda x, y, z: 1
    lim1 = lambda x: -minor*((1 - (x*x)/(r*r)) ** 0.5)
    lim2 = lambda x:  minor*((1 - (x*x)/(r*r)) ** 0.5)
    lim3 = lambda x, y: -minor2*((1 - (x*x)/(r*r) - (y*y)/(minor*minor)) ** 0.5)
    lim4 = lambda x, y:  minor2*((1 - (x*x)/(r*r) - (y*y)/(minor*minor)) ** 0.5)

    area = igr.dblquad(g, -r, r, lim1, lim2)
    volume = igr.tplquad(h, -r, r, lim1, lim2, lim3, lim4)

    perimeter = 2*np.pi * r if (r == minor) else np.pi * (3 * (r + minor) - np.sqrt((3 * r + minor) * (r + 3 * minor)))

#    print("Single integral is ", igr.quad(f, 0, 1))
    print("Area is ", area)
    print("Volume is ", volume)
    print("Perimeter is ", perimeter)
    # print("Exact volume = ", 4 / 3 * np.pi * r * minor * minor2)

    fig, ax = plt.subplots()

    theta = np.linspace(0, 2 * np.pi, 100)

    plt.plot(r * np.cos(theta), minor * np.sin(theta))
    plt.grid(color='lightgray', linestyle='--')
    plt.text(-r + 0.2*minor, 0.0, f"Area = {area[0]}")
    if not r == minor:
        plt.text(-r + 0.2, -0.2*minor, f"Circumference (approx.) = {perimeter}") # 2*np.pi*((r*r + minor*minor)/2)**0.5
    else:
        plt.text(-r + 0.2, -0.2*minor, f"Circumference = {perimeter}")

    ax.set_xlabel('x')
    ax.set_ylabel('y(x)')
    mr = max(r, minor)
    ax.set_xlim(-mr, mr)
    ax.set_ylim(-mr, mr)
    ax.set_title("Ellipse")
    plt.show()

    # Set of all spherical angles:
    phi = np.linspace(0, np.pi, 100)

    # Cartesian coordinates that correspond to the spherical angles:
    # (this is the equation of an ellipsoid):
    x = r * np.outer(np.cos(theta), np.sin(phi))
    y = minor * np.outer(np.sin(theta), np.sin(phi))
    z = minor2 * np.outer(np.ones_like(theta), np.cos(phi))

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    # Plot:
    ax.plot_wireframe(x, y, z, rstride=4, cstride=4, color='b')
    mr = max(r, minor, minor2)
    ax.set_xlim3d(-mr, mr)
    ax.set_ylim3d(-mr, mr)
    ax.set_zlim3d(-mr, mr)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z(x,y)')
    ax.set_title("Ellipsoid")
    plt.show()