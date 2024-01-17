#!/usr/bin/env python3
"""
Measure Runtime module
"""

import asyncio
import timeit

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension
    four times in parallel.
    """
    start_time = timeit.default_timer()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = timeit.default_timer()

    return end_time - start_time
