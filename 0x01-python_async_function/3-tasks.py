#!/usr/bin/env python3
"""
Implement a function that creates a task
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create a task

    Args:
        max_delay: maximum delay of the task

    Return:
        the created task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
