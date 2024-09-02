#!/usr/bin/env python3
"""
Implement a coroutine that execute four tasks concurrently
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute four tasks concurrently and measure the runtime

    Args: None

    Return:
        The runtime
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    return time.time() - start_time
