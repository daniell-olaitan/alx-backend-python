#!/usr/bin/env python3
"""
Implement a coroutine that spawns a coroutine a number of time
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn a coroutine a number of time

    Args:
        n: number of time to spawn the coroutine
        max_delay: the maximum delay of the coroutine

    Return:
        list of all the delays in ascending order
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
