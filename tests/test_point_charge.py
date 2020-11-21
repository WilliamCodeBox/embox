import matplotlib.pyplot as plt
import numpy as np
import pytest
from numpy.testing import assert_allclose

from embox.electrostatic import PointCharge
from embox.geomesh.vector import Vector


def test_location():
    c = PointCharge(1.0, Vector([0, 0, 0]))
    assert c.location == Vector([0, 0, 0])


@pytest.mark.skip("test for plot function of the PointCharge")
def test_plot():
    p = PointCharge(1.0, Vector([0, 0, 0]))
    p.plot()
    plt.show()


def test_mag():
    c = PointCharge(1.0, Vector([0, 0, 0]))
    assert c.coulomb == 1.0

    c.coulomb = 2.0
    assert c.coulomb == 2.0


def test_force_on_one_vs_one():
    c1 = PointCharge(1.0, np.array([0, 0, 0]))
    c2 = PointCharge(1.0, np.array([1, 0, 0]))

    f12 = c1.force_on(c2)
    assert_allclose(f12.length, 9.0E9)

    f21 = c2.force_on(c1)
    assert_allclose(f21.length, f12.length)

    assert f12 == -f21


def test_force_on_two_vs_one():
    c1 = PointCharge(1E-3, Vector([3, 2, -1]))
    c2 = PointCharge(-2E-3, Vector([-1, -1, 4]))
    c3 = PointCharge(10E-9, Vector([0, 3, 1]))

    f13 = c1.force_on(c3)
    f23 = c2.force_on(c3)

    ret = f13 + f23
    assert_allclose(ret.Ax, -6.512 * 1E-3, rtol=1E-3)
    assert_allclose(ret.Ay, -3.713 * 1E-3, rtol=1E-3)
    assert_allclose(ret.Az, 7.509 * 1E-3, rtol=1E-3)


def test_e_field_intensity():
    c1 = PointCharge(1E-3, Vector([3, 2, -1]))
    c2 = PointCharge(-2E-3, Vector([-1, -1, 4]))

    r = Vector([0, 3, 1])

    e1 = c1.e_field_intensity(r)
    e2 = c2.e_field_intensity(r)
    ret = e1 + e2

    assert_allclose(ret.Ax, -651.2 * 1E3, rtol=1E-3)
    assert_allclose(ret.Ay, -371.3 * 1E3, rtol=1E-3)
    assert_allclose(ret.Az, 750.9 * 1E3, rtol=1E-3)
