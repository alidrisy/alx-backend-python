#!/usr/bin/env python3
""" Model for type-annotated function make_multiplier """
from typing import Callable


def sqrt(num: float) -> float:
    """ Function that return the squer of float """
    return num * num


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Function that takes a float multiplier as argument and returns
    a function that multiplies a float by multiplier."""
    return sqrt
