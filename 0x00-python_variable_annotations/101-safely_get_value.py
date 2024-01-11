#!/usr/bin/env python3
""" Model for safely_get_value type-annotated function """
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] =
                     None) -> Union[Any, T]:
    """ Function to return dict elemnet or default value """
    if key in dct:
        return dct[key]
    else:
        return default
