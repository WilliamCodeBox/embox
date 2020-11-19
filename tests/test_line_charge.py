import matplotlib.pyplot as plt
import numpy as np
from embox.electrostatic import LineCharge
from embox.math import Vector
from numpy.testing import assert_allclose
from embox.geomesh.point import Point


def test_plot_line_segments():
    A = Vector(0, 0, 0)
    B = Vector(1, 1, 0)
    dx = 1.0 / 1000
    unit_vec = (B - A).unit
    increment = dx * unit_vec

    N = int(np.floor((B - A).mag / dx))

    fig, ax = plt.subplots(1, 1)
    for _ in range(N):
        ax.plot(A.x, A.y, "r*")
        A += increment

    # plt.show()


def test_e_field_intensity():
    A = Point([0, 0, 0])
    B = Point([1, 0, 0])
    C = Vector(0.5, 1, 0)

    rho = 1E-8
    line_charge = LineCharge(rho, A, B)

    field = line_charge.e_field_intensity(C, dx=1.0 / 100000.0)
    k = 9.0E9
    ret = (k * rho) / (np.sqrt(1.0 + 0.5 * 0.5))
    assert_allclose(field.x, 0.0, atol=1E-3)
    assert_allclose(field.y, ret, rtol=1E-3)
    assert_allclose(field.z, 0.0)
