#!/usr/bin/env python3
"""
Module implements an duck-typed annotated function
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Make sure the first element of a sequence is safe

    Args:
        lst: the given sequence

    Return:
        The first element if the sequence is valid OR
        None otherwise
    """
    if lst:
        return lst[0]
    else:
        return None
