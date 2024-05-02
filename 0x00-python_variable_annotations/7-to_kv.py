#!/usr/bin/env python3
'''
This function takes this string k and an int
OR float v and returns a tuple. This first element
of the tuple is the string k. The second element is
the square of the int/float v and should be annotated
as a float.
'''


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, v ** 2)
