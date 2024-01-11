#!/usr/bin/env python3

"""
This module contains a function 'safely_get_value',
with type annotations using TypeVar.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Returns the value associated with the given key in the dictionary 'dct'.
    If the key is not present, returns the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
