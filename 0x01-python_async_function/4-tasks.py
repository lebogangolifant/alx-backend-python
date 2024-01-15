#!/usr/bin/env python3
"""
Creating asyncio.Tasks using regular function syntax.
"""

import asyncio
from typing import List
from random import uniform

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates a list of asyncio.Tasks for the wait_random function,
    with the given max_delay.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
