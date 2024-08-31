#!/usr/bin/env python3
"""
Module implements a type-annotated function which takes a list of
floats as argument and returns their sum as a float.
"""
from typing import List
from functools import reduce


def sum_list(input_list: List[float]) -> float:
    """
    Compute the sum of the floats in a given list

    Args:
        mxd_lst: list of given floats

    Return:
        sum of the given floats
    """
    return reduce(lambda x, y: x + y, input_list)
