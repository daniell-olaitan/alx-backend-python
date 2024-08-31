#!/usr/bin/env python3
"""
Module implements a type-annotated function that takes a string
and an int OR float as arguments and returns a tuple
"""
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return k, v**2
