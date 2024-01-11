#!/usr/bin/env python3
""" Model to return the sum of float list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Function which takes a list mxd_list of floats and integers
    as argument and returns their sum as a float. """
    x: float = 0.0
    for i in mxd_lst:
        x += i
    return x
