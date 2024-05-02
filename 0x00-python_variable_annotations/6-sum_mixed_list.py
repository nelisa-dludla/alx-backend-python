#!/usr/bin/env python3
'''
This function returns the sum of a list of
mixed integers and float as a float
'''


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    sum: float = 0
    for num in mxd_lst:
        sum += num

    return sum
