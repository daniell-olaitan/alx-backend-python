#!/usr/bin/env python3
"""
Implement a coroutine that implement an async comprehension
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Implement an async comprehension

    Args: None

    Return:
        List of random numbers"
    """
    random_numbers = [rand_n async for rand_n in async_generator()]

    return random_numbers
