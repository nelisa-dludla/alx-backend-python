#!/usr/bin/env python3
'''
This function returns a function that multiples
a float by multiplier
'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def product(value: float) -> float:
        return value * multiplier
    return product
