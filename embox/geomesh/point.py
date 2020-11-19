"""
Fundamental point object in cartesian coordinate system
"""
from typing import Union

import numpy as np

from ..math.vector import Vector


class Point(object):
    dim = 0

    def __init__(self, loc: Union[Vector, list, np.ndarray]):
        self._set_loc(loc)

    @property
    def location(self) -> Vector:
        return self._loc

    @location.setter
    def location(self, loc: Union[Vector, list, np.ndarray]):
        self._set_loc(loc)

    def __str__(self):
        return f"[EMBOX] Point object {self._loc}"

    def _set_loc(self, loc: Union[Vector, list, np.ndarray]):
        if len(loc) > 3:
            raise ValueError("loc must be 3-element list or ndarray")
        if isinstance(loc, Vector):
            self._loc = loc
        else:
            if len(loc) == 2:
                self._loc = Vector(*loc, 0.0)
            else:
                self._loc = Vector(*loc)

    def __getitem__(self, index: int):
        assert 0 <= index <= 2
        return self.location[index]
