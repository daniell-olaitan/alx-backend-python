#!/usr/bin/env python3
"""
Implement a coroutine that delays for a given number seconds
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a given amount of seconds and the returns the time

    Args:
        max_delay: maximum amount of seconds

    Return:
        the amount of seconds waited
    """
    wait_time = random.uniform(0.0, max_delay)
    await asyncio.sleep(wait_time)

    return wait_time
