#!/usr/bin/env python3
""" Model for async_generator coroutine function """
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """ Generator function that return random numbers """
    for s in range(10):
        await asyncio.sleep(1)
        i = random.uniform(0, 10)
        yield i
