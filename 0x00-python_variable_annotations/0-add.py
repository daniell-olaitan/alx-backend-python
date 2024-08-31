#!/usr/bin/env python3
"""
Module implements a type-annotated function that takes two floats as
arguments and returns their sum as a float.
"""


def add(a: float, b: float) -> float:
    """
    Compute the sum of two given floats

    Args:
        a: first given float
        b: second given float

    Return:
        Sum of the given floats
    """
    return a + b
