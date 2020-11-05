#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta information
NAME = "empy"
DESCRIPTION = "Fundamentals of Electromagnetic with Python"
URL = "https://github.com/WilliamCodeBox/empy"
EMAIL = "codequote@163.com"
AUTHOR = "WilliamCodeBox"
REQUIRES_PYTHON = ">=3.6.0"
VERSION = "1.0.0"

# Required packages for this module to be executed
REQUIRED = []

# Optional packages
EXTRAS = []

# ######################## Functionalities ########################
here = os.path.abspath(os.path.dirname(__file__))

# Import README and use it as the long-description
# NOTE: this will only work if 'REAME.md' is present in MANIFEST.in file


