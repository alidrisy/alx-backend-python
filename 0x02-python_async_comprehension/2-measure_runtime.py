#!/usr/bin/env python3
""" Model for measure_runtime coroutine function """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Function that execute async_comprehension four times in parallel
    using asyncio.gather and measure the total runtime and return it. """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.perf_counter() - start
    return end
