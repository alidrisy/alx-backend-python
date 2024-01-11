#!/usr/bin/env python3
""" Model to return the sum of float list """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Function which takes a list input_list of floats as argument
    and returns their sum as a float. """
    x: float = 0.0
    for i in input_list:
        x += i
    return x
