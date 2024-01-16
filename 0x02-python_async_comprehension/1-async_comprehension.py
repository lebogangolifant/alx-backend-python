#!/usr/bin/env python3
"""
Async comprehension module
"""

from typing import List
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehensions
    """
    return [random_number async for random_number in async_generator()]
