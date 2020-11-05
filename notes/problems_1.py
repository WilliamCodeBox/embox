"""
This module contains some exercises
"""

from typing import Union

import matplotlib.pyplot as plt
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


if __name__ == '__main__':
    # ex1()
    ex2()
    print(f"-50 degrees in Celsius equals to {ex3(-50)} degrees in Fahrenheit.")
