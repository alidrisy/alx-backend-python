#!/usr/bin/env python3
""" Model for element_length type-annotated function """
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Function take an object and return list of tuple """
    return [(i, len(i)) for i in lst]
