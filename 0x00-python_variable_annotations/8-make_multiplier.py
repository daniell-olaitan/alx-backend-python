#!/usr/bin/env python3
"""
Module implements a type-annotated function that takes a
float as argument and returns a function that multiplies a float
"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda x: x * multiplier
