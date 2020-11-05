"""
This module contains some plot helper functions
"""
import matplotlib.pyplot as plt
from empy import Vector


def plot_vector_addition(ax: plt.Axes, v1: Vector, v2: Vector):
    v3 = v1 + v2

    ax.quiver(0., 0., 0., v1.x, v1.y, v1.z)
    ax.arrow(v1.x, v1.y, v1.z, v2.x, v2.y, v2.z)
    ax.arrow(0., 0., 0., v3.x, v3.y, v3.z)

    return ax
