#!/usr/bin/env python3
"""
Asynchronous coroutine for spawning multiple wait_random calls concurrently.
"""

import asyncio
from typing import List
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    An asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds (inclusive) and returns it.
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.
    Returns the list of all the delays in ascending order.
    """
    delays = []

    # Create a list of tasks
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Execute tasks concurrently
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
