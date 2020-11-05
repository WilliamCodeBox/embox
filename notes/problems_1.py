"""
This module contains some exercises
"""
from empy import plot_vector_addition
from empy import Vector
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

A = Vector(3, 4, 5)
B = Vector(-5, 4, -3)
fig, ax = plt.subplots(1, 1, projection="3d")
plot_vector_addition(ax, A, B)
plt.show()

