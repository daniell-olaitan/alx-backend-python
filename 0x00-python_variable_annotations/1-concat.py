#!/usr/bin/env python3
"""
Module implements a type-annotated function concat that takes two
strings as arguments and returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenate the given strings

    Args:
        str1: first string
        str2: second_string

    Return:
        The concatenated string
    """
    return str1 + str2
