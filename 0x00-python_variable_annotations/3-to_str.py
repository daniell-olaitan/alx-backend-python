#!/usr/bin/env python3
"""
Module implements a type-annotated function that takes a float as an
argument and returns the string representation of the float.
"""


def to_str(n: float) -> str:
    """
    Convert a given float to string

    Args:
        n: the given float

    Return:
        the string of the given float
    """
    return str(n)
