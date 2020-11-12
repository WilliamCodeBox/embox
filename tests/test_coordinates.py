from embox.math.coordinates import Cartesian
from scipy.constants import pi


def test_cartesian_to_cylindrical():
    point_ca = Cartesian(1, 0, 0)
    point_cy = point_ca.to_cylindrical()
    assert point_cy.rho == 1
    assert point_cy.phi == 0
    assert point_cy.z == 0


def test_cartesian_to_spherical():
    point_ca = Cartesian(1, 0, 0)
    point_sp = point_ca.to_spherical()
    assert point_sp.r == 1
    assert point_sp.theta == pi / 2.0
    assert point_sp.phi == 0
