#!/usr/bin/env python3
""" Model for task_wait_n asynchronous coroutine function """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function task_wait_n that call task_wait_random and return
    list of all the delays
    """
    tasks = [task_wait_random(max_delay) for i in range(n)]
    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
