import numpy as np
from embox import Vector


def z(x: float, y: float) -> float:
    return np.exp(- x ** 2 - y ** 2)


def del_z(x: float, y: float) -> Vector:
    x_component = -2 * x * np.exp(-x ** 2 - y ** 2)
    y_component = -2 * y * np.exp(-x ** 2 - y ** 2)
    return Vector(x_component, y_component, 0.0)


if __name__ == '__main__':
    # evaluate del_z at point (0, 0)
    print(r"grad_z(0, 0) = {}".format(del_z(0, 0)))
