#!/usr/bin/env python3

"""
This module contains a function 'safe_first_element'
with duck-typed annotations.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the input sequence if it exists,
    otherwise returns None.
    """
    if lst:
        return lst[0]
    else:
        return None
