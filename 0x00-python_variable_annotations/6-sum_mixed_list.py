#!/usr/bin/env python3
"""
Module implements a type-annotated function which takes a list of
integers and floats and returns their sum as a float.
"""
from typing import List, Union
from functools import reduce

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return reduce(lambda x, y: x + y, mxd_lst)
