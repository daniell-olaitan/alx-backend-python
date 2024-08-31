#!/usr/bin/env python3
"""
Module implements an annotated function
"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely gets a value from a dictionary

    Args:
        dct: the given dictionary
        key: the key to the value to search for in the dictionary
        default: the default value

    Return:
        the mapped value to `key` or default
    """
    if key in dct:
        return dct[key]
    else:
        return default
