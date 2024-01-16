#!/usr/bin/env python3
"""
Measure Runtime module
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension
    four times in parallel.
    """
    start_time = time.time()

    await asyncio.gather(
        *[async_comprehension() for _ in range(4)]
    )

    end_time = time.time()
    total_runtime = end_time - start_time

    return total_runtime