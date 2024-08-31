#!/usr/bin/env python3
"""
Module implements a type-annotated function which takes a float as
argument and returns the floor of the float.
"""
import math


def floor(n: float) -> int:
    """
    Convert a given float to its int floor

    Args:
        n: the given float

    Return:
        the floor of the given float
    """
    return math.floor(n)
