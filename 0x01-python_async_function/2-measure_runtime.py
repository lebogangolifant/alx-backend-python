#!/usr/bin/env python3
"""
Measure runtime for wait_n function.
"""

import asyncio
import time
import importlib
from typing import List

# Import wait_n dynamically
wait_n_module = importlib.import_module('1-concurrent_coroutines')
wait_n = wait_n_module.wait_n


async def wait_n_async(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous version of wait_n that returns a list of delays.
    """
    return await wait_n(n, max_delay)


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay) and,
    return total_time / n.
    """
    start = time.perf_counter()

    asyncio.run(wait_n_async(n, max_delay))

    total_time = time.perf_counter() - start
    return total_time / n
