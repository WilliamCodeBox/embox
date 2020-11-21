import numpy as np

from embox.geomesh.point import Point
from embox.geomesh.vector import Vector


def test_xyz_getter_setter():
    p = Point((1, 2, 3))
    assert p.x == 1
    assert p.y == 2
    assert p.z == 3
    p.x = 3
    p.y = 2
    p.z = 1
    assert p.x == 3
    assert p.y == 2
    assert p.z == 1


def test_to_spherical():
    point_ca = Point([1, 0, 0])
    point_sp = point_ca.to_spherical()
    assert point_sp[0] == 1
    assert point_sp[1] == np.pi / 2.0
    assert point_sp[2] == 0


def test_to_cylindrical():
    point_ca = Point([1, 0, 0])
    point_cy = point_ca.to_cylindrical()
    assert point_cy[0] == 1
    assert point_cy[1] == 0
    assert point_cy[2] == 0


def test_location():
    p = Point([1, 2, 3])
    vec = p.view(Vector)
    assert vec.Ax == 1
    assert vec.Ay == 2
    assert vec.Az == 3
