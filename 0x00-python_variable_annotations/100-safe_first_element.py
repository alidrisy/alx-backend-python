#!/usr/bin/env python3
"""Model for safe_first_element type-annotated function """
from typing import Sequence, Union, Any, NewType

NoneType = NewType('NoneType', None)


def safe_first_element(lst: Sequence[any]) -> Union[Any, NoneType]:
    """ Function to return first elemnt in a sequence or none"""
    if lst:
        return lst[0]
    else:
        return None
