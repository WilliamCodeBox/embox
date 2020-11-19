import embox.postprocessor.plot as ep
import matplotlib.pyplot as plt
import numpy as np
from embox.postprocessor.plot import plot_curve, plot_ax


def test_subplot():
    fig, ax = ep.subplots(1, 1)
    t = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(2 * np.pi * 1E6 * t)
    ax.plot(t, y, "r")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    # plt.show()


def test_plot_curve():
    t = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(2 * np.pi * 1E6 * t)
    z = np.sin(2 * np.pi * 10E6 * t + np.pi / 2)
    # plot_curve(t, y, x_label="x", y_label='y', fig_title="title")
    # plot_curve(t, y, t, z, x_label="x", y_label='y', fig_title="title")


def test_plot_ax():
    t = np.linspace(0, 10E-6, 200)
    y = np.sin(2 * np.pi * 1E6 * t)
    z = np.sin(2 * np.pi * 10E6 * t)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 3), dpi=300)
    plot_ax(ax1, t, y)
    plot_ax(ax2, t, z)
    plt.tight_layout()
    # plt.show()
