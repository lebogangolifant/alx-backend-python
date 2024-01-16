#!/usr/bin/env python3
"""
Async generator module
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generates 10 random floats with a 1-second delay
    """
    for _ in range(10):
        yield random.random()
        await asyncio.sleep(1)
