#!/usr/bin/env python3
"""
Module implements an annotated function
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zoom in a given array

    Args:
        lst: the given array to be zoomed
        factor: zoom factor

    Return:
        A list of the zoomed array
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = 12, 72, 91

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
