import numpy as np
from empy.electrostatic import Charge
from empy.math import Vector
from numpy.testing import assert_allclose
from numpy.testing import assert_raises


def test_init_raise_value_error():
    with assert_raises(ValueError):
        c = Charge(1.0, np.ndarray([1, 2, 3, 4]))
        c = Charge(1.0, np.ndarray([1, 2]))


def test_loc():
    c = Charge(1.0, Vector(0, 0, 0))
    assert c.loc == Vector(0, 0, 0)

    c.loc = Vector(1, 0, 0)
    assert c.loc == Vector(1, 0, 0)


def test_mag():
    c = Charge(1.0, Vector(0, 0, 0))
    assert c.mag == 1.0

    c.mag = 2.0
    assert c.mag == 2.0


def test_force_on():
    c1 = Charge(1.0, np.array([0, 0, 0]))
    c2 = Charge(1.0, np.array([1, 0, 0]))

    f12 = c1.force_on(c2)
    assert_allclose(f12[0], 9.0E9)

    f21 = c2.force_on(c1)
    assert_allclose(f12[0], f12[0])

    r12 = f12[1] - f12[2]
    r21 = f21[1] - f21[2]
    assert r12 == -r21
