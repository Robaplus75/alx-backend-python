#!/usr/bin/env python3
""" functions"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make mulitplier func"""
    def f(n: float) -> float:
        """f func"""
        return float(n * multiplier)
    return f
