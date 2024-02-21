#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
from functools import wraps
import requests
from typing import (
    Mapping, Sequence,
    Any, Dict,
    Callable,
)

__all__ = [
    "access_nested_map", "get_json", "memoize",
]


def get_json(url: str) -> Dict:
    """gests json form a remote url
    """
    response = requests.get(url)
    return response.json()


def memoize(fn: Callable) -> Callable:
    """
    >>> my_object = MyClass()
    >>> my_object.a_method
    a_method called
    42
    >>> my_object.a_method
    42
    """
    attr_name = "_{}".format(fn.__name__)

    @wraps(fn)
    def memoized(self):
        """"wraps"""
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return property(memoized)


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """
    >>> nested_map = {"a": {"b": {"c": 1}}}
    >>> access_nested_map(nested_map, ["a", "b", "c"])
    1
    """
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]

    return nested_map
