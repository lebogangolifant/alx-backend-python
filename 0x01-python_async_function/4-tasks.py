#!/usr/bin/env python3
"""
Creating asyncio.Tasks using regular function syntax.
"""

import asyncio
from typing import List
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    An asynchronous coroutine that simulates waiting for a random delay.
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for the wait_random function,
    with the given max_delay.
    """
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates a list of asyncio.Tasks for the wait_random function,
    with the given max_delay.
    """
    return await asyncio.gather(*(task_wait_random(max_delay) for _ in range(n)))
