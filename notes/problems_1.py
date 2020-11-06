"""
This module contains some exercises
"""

from typing import Union

import matplotlib.pyplot as plt
import numpy as np
from empy import Vector
from empy import plot_vector_addition


def ex1():
    """
    Given two vectors A and B, find C=A+B and D=A-B.
    Illustrate these vectors.

    :return:
    """
    A = Vector(3, 4, 5)
    B = Vector(-5, 4, -3)
    fig = plt.figure()
    ax1 = fig.add_subplot(121, projection="3d")
    plot_vector_addition(ax1, A, B)

    ax2 = fig.add_subplot(122, projection="3d")
    plot_vector_addition(ax2, A, -B)
    plt.show()


def ex2():
    """
    Using the vectors in ex1, evaluate A.dot(B) and A.cross(B).
    :return:
    """
    A = Vector(3, 4, 5)
    B = Vector(-5, 4, -3)
    print(f"The dot product of A and B is {A.dot(B)}")
    print(f"The cross product of A and B is {A.cross(B)}")


def ex3(degrees_in_celsius: Union[int, float]) -> float:
    """
    Convert degrees in Celsius to degrees in Fahrenheit.
    One Celsius equals to 33.8 Fahrenheit.
    :return:
    """
    return degrees_in_celsius * 1.8 + 32.


def ex4(yard: Union[int, float]) -> float:
    """
    Convert yardstick to meters.
    :param yard:
    :return:
    """
    return yard * 0.9144


def ex5():
    """
    Plot exp(-x) on a linear and a semilog graph.
    :return:
    """
    x = np.linspace(0, 100, 500)
    y = np.exp(-x)
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(x, y)
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_title("linear plot")
    ax1.grid()

    ax2.plot(x, y)
    ax2.set_yscale("log")
    ax2.set_xlabel("x")
    # ax2.set_ylabel("y")
    ax2.set_title("semilog plot")
    ax2.grid()

    plt.tight_layout()
    plt.show()


def ex6():
    """
    plot two cycles of cos(x) on a linear and a polar graph.
    :return:
    """
    f = 0.5 / np.pi
    T = 1.0 / f
    x = np.linspace(0, 2 * T, 100)
    y = np.cos(x)

    thetas = np.arctan2(y, x)
    rs = np.sqrt(x * x + y * y)

    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax1.plot(x, y)

    ax2 = fig.add_subplot(122, projection="polar")
    ax2.plot(thetas, rs)
    plt.show()


def ex7():
    """
    Plot a vector field defined by y^2 u_x - x u_y in the region -2< x < +2 and -2 < y < +2
    The length of the vectors in the field should be proportional to the field at that point.
    :return:
    """
    x = np.linspace(-2, 2, 30)
    y = np.linspace(-2, 2, 30)

    X, Y = np.meshgrid(x, y)
    U = Y * Y  # x-components
    V = -X  # y-components

    fig, ax = plt.subplots(1, 1)
    ax.quiver(x, y, U, V, units="width")
    ax.set_title("Vector field $y^2\\vec{u}_x - x \\vec{u}_y$")
    plt.show()


def ex8():
    """
    Plot a vector field defined by sinx u_x - siny u_y in the region 0 < x < pi and 0 < y < pi.
    The length of the vectors in the field should be proportional to the field at that point.
    :return:
    """
    x = np.linspace(0, np.pi, 25)
    y = np.linspace(0, np.pi, 25)

    X, Y = np.meshgrid(x, y)
    U = np.sin(X)
    V = -np.sin(Y)

    fig, ax = plt.subplots(1, 1)
    ax.quiver(X, Y, U, V, units="width")
    ax.set_title("Vector field $sin(x)\\vec{u}_x - sin(y)\\vec{u}_y$")
    plt.show()


def ex9():
    """
    Find the scalar product of A = 3u_x + 4u_y + 5u_z and B = -5u_x + 4u_y - 3u_z.
    Determine the angle between A and B.
    :return:
    """
    A = Vector(3, 4, 5)
    B = Vector(-5, 4, -3)
    C = A.dot(B)

    print(f"Scalar product of {A} and {B} is {C}")

    proj = A.projection(B)
    angle = np.arccos(proj / A.mag)

    print(f"Angle between A and B is {angle * 180 / np.pi} in degrees")


def ex10():
    """
    For vectors A = u_x + u_y + u_z, B = 2ux + 2uy + 2uz and C = 3ux + 3uy + 3uz,
    show that A X (B X C) = B(A*C) - C(A*B)
    :return:
    """
    A = Vector(1, 1, 1)
    B = Vector(2, 2, 2)
    C = Vector(3, 3, 3)

    lhs = A.cross(B.cross(C))
    rhs = B * A.dot(C) - C * A.dot(B)

    print(f"A X (B X C) = {lhs}")
    print(f"B(A*C) - C(A*B) = {rhs}")


def ex11():
    """
    A = (1, 3, 5), B = (2, 4, 6), C = (3, 4, 5)
    show that A X (B X C) = B(A*C) - C(A*B)
    :return:
    """
    A = Vector(1, 3, 5)
    B = Vector(2, 4, 6)
    C = Vector(3, 4, 5)

    lhs = A.cross(B.cross(C))
    rhs = B * A.dot(C) - C * A.dot(B)

    print(f"A X (B X C) = {lhs}")
    print(f"B(A*C) - C(A*B) = {rhs}")


def ex12():
    """

    :return:
    """


if __name__ == '__main__':
    # ex1()
    ex2()
    print(f"-50 degrees in Celsius equals to {ex3(-50)} degrees in Fahrenheit.")
    print(f"35 yards equals to {ex4(35)} meters")
    # ex5()
    # ex6()
    # ex7()
    # ex8()
    # ex9()
    ex10()
    ex11()
