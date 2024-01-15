#!/usr/bin/env python3
""" Model for wait_n asynchronous coroutine function """
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Function measure_time that call wait_a and measure an
    approximate elapsed time.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter() - start
    return end / n
