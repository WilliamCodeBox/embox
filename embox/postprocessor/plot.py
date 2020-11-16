"""
This module contains some plot helper functions
"""

from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

from ._config import rcParams, formatter
from ..math.vector import Vector

plt.rcParams = rcParams


def plot_vector_addition(ax: plt.Axes, v1: Vector, v2: Vector, **kwargs):
    v3 = v1 + v2

    ax.quiver(0., 0., 0., v1.x, v1.y, v1.z, **kwargs)
    ax.quiver(v1.x, v1.y, v1.z, v2.x, v2.y, v2.z, **kwargs)
    ax.quiver(0., 0., 0., v3.x, v3.y, v3.z, **kwargs)

    return ax


def plot_curve(x: np.ndarray, y: np.ndarray, *args, **kwargs):
    """
    plot 2D curve, if the keyword fig_name is provided, the figure will be saved
    :param x: the x-axis ndarray
    :param y: the y-axis ndarray
    :param kwargs: kwargs for plt.plot and some custom kwargs including the x_label, y_label, fig_title, fig_name
    :return:
    """
    if len(x) != len(y):
        raise ValueError("The input arrays must have the same length")
    if len(args) % 2 != 0:
        raise ValueError("The number of extras arrays must be even number")

    if "x_scale" in kwargs.keys():
        x_scale = kwargs["x_scale"]
        kwargs.pop("x_scale")
    else:
        x_scale = 1.0

    if "y_scale" in kwargs.keys():
        y_scale = kwargs["y_scale"]
        kwargs.pop("y_scale")
    else:
        y_scale = 1.0

    if "x_label" in kwargs.keys():
        x_label = kwargs["x_label"]
        kwargs.pop("x_label")
    else:
        x_label = ""

    if "y_label" in kwargs.keys():
        y_label = kwargs["y_label"]
        kwargs.pop("y_label")
    else:
        y_label = ""

    if "fig_title" in kwargs.keys():
        fig_title = kwargs["fig_title"]
        kwargs.pop("fig_title")
    else:
        fig_title = ""

    if "fig_name" in kwargs.keys():
        fig_name = kwargs["fig_name"]
        kwargs.pop("fig_name")
    else:
        fig_name = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if "dpi" in kwargs.keys():
        dpi = kwargs["dpi"]
        kwargs.pop("dpi")
    else:
        dpi = 100
    fig, ax = plt.subplots(1, 1, figsize=(16, 9))
    ax.plot(x_scale * x, y_scale * y, **kwargs)
    if len(args) != 0:
        for ii in range(0, len(args), 2):
            ax.plot(x_scale * args[ii], y_scale * args[ii + 1], **kwargs)
    ax.yaxis.set_major_formatter(formatter)
    ax.set_xlabel(x_label, fontsize=20)
    ax.set_ylabel(y_label, fontsize=20)
    ax.set_title(fig_title, fontsize=20)
    ax.xaxis.set_tick_params(labelsize=16)
    ax.yaxis.set_tick_params(labelsize=16)
    plt.tight_layout()
    plt.savefig(fig_name, dpi=dpi)
    plt.close()


def plot_ax(ax: plt.Axes, x: np.ndarray, y: np.ndarray, **kwargs) -> plt.Axes:
    """
    Plot x-y with given axes
    :param ax: the axes to plot
    :param x: the x-axis array
    :param y: the y-axis array
    :param kwargs:
    :return:
    """
    if "x_scale" in kwargs.keys():
        x_scale = kwargs["x_scale"]
        kwargs.pop("x_scale")
    else:
        x_scale = 1.0

    if "y_scale" in kwargs.keys():
        y_scale = kwargs["y_scale"]
        kwargs.pop("y_scale")
    else:
        y_scale = 1.0

    if "x_label" in kwargs.keys():
        x_label = kwargs["x_label"]
        kwargs.pop("x_label")
    else:
        x_label = ""

    if "y_label" in kwargs.keys():
        y_label = kwargs["y_label"]
        kwargs.pop("y_label")
    else:
        y_label = ""

    if "fig_title" in kwargs.keys():
        fig_title = kwargs["fig_title"]
        kwargs.pop("fig_title")
    else:
        fig_title = ""

    with plt.style.context(['science', 'ieee', "retro"]):
        ax.plot(x_scale * x, y_scale * y, **kwargs)
        ax.yaxis.set_major_formatter(formatter)
        ax.set_xlabel(x_label, fontsize=14)
        ax.set_ylabel(y_label, fontsize=14)
        ax.set_title(fig_title, fontsize=14)
        ax.grid()
        ax.xaxis.set_tick_params(labelsize=8)
        ax.yaxis.set_tick_params(labelsize=8)
    return ax
