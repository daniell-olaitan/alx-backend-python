#!/usr/bin/env python3
"""
Implement a coroutine that measures the total execution time of
another coroutine
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time of a coroutine

    Args:
        n: number of time to spawn the coroutine
        max_delay: the maximum delay of the coroutine

    Return:
        the average execution time
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
