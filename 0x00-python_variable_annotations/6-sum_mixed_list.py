#!/usr/bin/env python3

"""
This module contains a function 'sum_mixed_list'
that calculates the sum of a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list of integers and floats.
    """
    return sum(mxd_lst)
