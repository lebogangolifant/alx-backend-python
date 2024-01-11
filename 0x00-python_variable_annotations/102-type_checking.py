#!/usr/bin/env python3

"""
This module contains a function 'zoom_array' with corrected type annotations.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on the given tuple by repeating each item 'factor' times.
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
