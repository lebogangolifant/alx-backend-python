#!/usr/bin/env python3

"""
This module contains a function 'element_length'
with annotated parameters and return values.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotates the parameters and return values of the element_length function.
    """
    return [(i, len(i)) for i in lst]
