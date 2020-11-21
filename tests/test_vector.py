import numpy as np
from numpy.testing import assert_allclose

from embox.geomesh.vector import Vector


def test_xyz():
    a = Vector([1, 2, 3])
    assert a.Ax == 1
    assert a.Ay == 2
    assert a.Az == 3


def test_vector_equal():
    a = Vector([1, 2, 3])
    b = Vector((1, 2, 3))
    assert a == b


def test_vector_addition():
    a = Vector(np.array([3, 0, 0]))
    b = Vector([0, 4, 0])
    c = a + b
    assert_allclose(c.Ax, 3)
    assert_allclose(c.Ay, 4)
    assert_allclose(c.Az, 0)


def test_vector_magnitude():
    c = Vector([3, 4, 0])
    assert_allclose(c.norm, 5)


def test_vector_unit_vec():
    a = Vector([3, 4, 0])
    assert a.unit == Vector([0.6, 0.8, 0])


def test_vector_dot_product():
    a = Vector([2, 0, 0])
    b = Vector([1, 2, 0])
    assert_allclose(a.dot(b), 2)


def test_vector_perpendicular():
    a = Vector([1, 2, 3])
    b = 3 * a
    assert a.parallel_to(b)
