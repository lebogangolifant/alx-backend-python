#!/usr/bin/env python3

"""
This module contains a function 'make_multiplier'
that takes a float multiplier and returns a function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier and returns a function
    that multiplies a float by multiplier.
    """

    def multiplier_function(x: float) -> float:
        """
        Inner function that multiplies a float by the given multiplier.
        """
        return x * multiplier

    return multiplier_function
