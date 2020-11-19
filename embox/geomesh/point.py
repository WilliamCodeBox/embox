"""
Fundamental point object in cartesian coordinate system
"""
from typing import Union

import numpy as np


class Point(object):
    dim = 0

    def __init__(self, loc: Union[list, np.ndarray]):
        self._set_loc(loc)

    @property
    def location(self) -> np.ndarray:
        return self._loc

    @location.setter
    def location(self, loc: Union[list, np.ndarray]):
        self._set_loc(loc)

    def __str__(self):
        return f"[EMBOX] Point object {self._loc}"

    def _set_loc(self, loc: Union[list, np.ndarray]):
        if len(loc) > 3:
            raise ValueError("loc must be 3-element list or ndarray")
        if len(loc) == 2:
            self._loc = np.array([*loc, 0.0])
        else:
            self._loc = np.array([*loc])
