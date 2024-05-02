#!/usr/bin/env python3
'''
This function returns the sum of a list
of floats as a float
'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Returns the sum of input_list as a float'''
    sum: float = 0
    for num in input_list:
        sum += num

    return sum
