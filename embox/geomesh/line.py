"""
Fundamental straight line object in cartesian coordinate system
"""
from typing import Union

import numpy as np

from ..math.vector import Vector


class Line(object):
    def __init__(self, start: Union[Vector, list, np.ndarray], end: Union[Vector, list, np.ndarray]):
        """
        Straight line form start to end
        :param start: the start point of the line
        :param end: the end point of the line
        """
        self._start = start
        self._end = end

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start: Union[Vector, list, np.ndarray]):
        self._start = start