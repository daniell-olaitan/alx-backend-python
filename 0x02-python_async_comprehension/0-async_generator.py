#!/usr/bin/env python3
"""
Implement a coroutine that asyncronously wait 1 sec and yield a random number
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asyncronously wait 1 sec and yield a random number

    Args: None

    Yield:
        Randomly generated number
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0.0, 10.0)
