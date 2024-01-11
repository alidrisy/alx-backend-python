#!/usr/bin/env python3
""" Model for zoom_array type-annotated function """
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Function that return list from tuple and factor int """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
