#!/usr/bin/python
# -*- coding: utf-8 -*-

"""pybline module."""


from pkg_resources import get_distribution

from scipy import constants

from . import (
    models,
    tools
)

# Gravity in cm/sec/sec
GRAV = constants.g / constants.centi


__author__ = 'Albert Kottke'
__copyright__ = 'Copyright 2018 Albert Kottke'
__license__ = 'MIT'
__title__ = 'pybline'
__version__ = get_distribution('pybline').version
