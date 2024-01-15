#!/usr/bin/env python3
""" Model for wait_random asynchronous coroutine function """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Takes in an integer argument and waits for a random
    delay between 0 and the argument """
    t = random.uniform(0, max_delay)
    await asyncio.sleep(t)
    return t
