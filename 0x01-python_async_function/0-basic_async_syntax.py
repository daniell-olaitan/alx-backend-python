#!/usr/bin/env python3
"""
Implement a coroutine that delays for a given number seconds
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    wait_time = random.uniform(0.0, max_delay)
    await asyncio.sleep(wait_time)

    return wait_time
