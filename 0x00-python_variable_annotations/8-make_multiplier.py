#!/usr/bin/env python3
'''
This function returns a function that multiples
a float by multiplier
'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Returns the square of multiplier'''
    def product(value: float) -> float:
        '''Returns the square of value'''
        return value * multiplier
    return product
