#!/usr/bin/env python3
from typing import Callable
"""takes in a function and return a function"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
