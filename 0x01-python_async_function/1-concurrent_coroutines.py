#!/usr/bin/env python3
""" Model for wait_n asynchronous coroutine function """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function wait_n that call wait_random and return list of all the delays
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
