#!/usr/bin/env python3
"""
Asynchronously waits for random delays
"""

from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Waits for random delays up to max_delay and returns a list of actual delays
    """
    delay_list = []

    async def collect_delay(task: asyncio.Task) -> None:
        delay_list.append(await task)

    spawn_list = [task_wait_random(max_delay) for _ in range(n)]

    for spawn in spawn_list:
        asyncio.ensure_future(collect_delay(spawn))

    await asyncio.gather(*spawn_list)

    return delay_list
