import matplotlib.pyplot as plt
import pytest

import embox.postprocessor.plot as ep
from embox.geomesh.vector import Vector


@pytest.mark.skip("test for plot_vector")
def test_plot_vector():
    vec = Vector(1.0, 1.0, 1.0)

    fig = plt.figure()
    ax = fig.gca(projection="3d")
    xs = [0.0, vec.x]
    ys = [0.0, vec.y]
    zs = [0.0, vec.z]
    arrow = ep.Arrow3D(xs, ys, zs, mutation_scale=20, arrowstyle="-|>", lw=1, color="r")
    ax.add_artist(arrow)
    plt.show()


@pytest.mark.skip("test for plot vector addition")
def test_plot_vector_addition():
    v1 = Vector(1.0, 1.0, 0.0)
    v2 = Vector(1.0, 1.0, 1.0)
    v3 = v1 + v2



    plt.show()


@pytest.mark.skip("Test for plot cube")
def test_cube():
    r = Vector(0, 0, 0)
    length = 2
    ep.cube(r, length, color="b")
    plt.show()
