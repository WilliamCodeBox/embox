import matplotlib.pyplot as plt
import numpy as np
from embox.postprocessor import plot_curve, plot_ax


def test_plot_curve():
    t = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(2 * np.pi * 1E6 * t)
    z = np.sin(2 * np.pi * 10E6 * t + np.pi / 2)
    plot_curve(t, y)
    plot_curve(t, y, t, z)


def test_plot_ax():
    t = np.linspace(0, 10E-6, 200)
    y = np.sin(2 * np.pi * 1E6 * t)
    z = np.sin(2 * np.pi * 10E6 * t)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 3), dpi=300)
    plot_ax(ax1, t, y)
    plot_ax(ax2, t, z)
    plt.tight_layout()
    plt.show()
