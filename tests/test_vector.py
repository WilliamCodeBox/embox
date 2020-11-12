from embox import Vector
from numpy.testing import assert_allclose


def test_vector_equal():
    a = Vector(1, 2, 3)
    b = Vector(1, 2, 3)
    assert a == b


def test_vector_addition():
    a = Vector(3, 0, 0)
    b = Vector(0, 4, 0)
    c = a + b
    assert_allclose(c.x, 3)
    assert_allclose(c.y, 4)
    assert_allclose(c.z, 0)


def test_vector_magnitude():
    c = Vector(3, 4, 0)
    assert_allclose(c.norm2, 5)


def test_vector_unit_vec():
    a = Vector(3, 4, 0)
    assert a.unit == Vector(0.6, 0.8, 0)


def test_vector_dot_product():
    a = Vector(2, 0, 0)
    b = Vector(1, 2, 0)
    assert_allclose(a.dot(b), a * b)
    assert_allclose(a.dot(b), 2)


def test_vector_perpendicular():
    a = Vector(1, 2, 3)
    b = 3 * a
    assert a.parallel_to(b)
