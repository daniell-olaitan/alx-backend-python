#!/usr/bin/env python3
"""
Module implements an annotated function
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Computes the length of the given iterable

    Args:
        lst: the given iterable

    Returns:
        List of a tuple of the elements and their corresponding length
    """
    return [(i, len(i)) for i in lst]
