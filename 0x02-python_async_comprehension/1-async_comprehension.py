#!/usr/bin/env python3
""" Model for async_comprehension coroutine function """
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Function that call async_generator and return a list of float """
    return [i async for i in async_generator()]
