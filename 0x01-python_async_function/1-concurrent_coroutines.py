#!/usr/bin/env python3
'''
This is an async routinue
'''

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    '''Returns a list of delays'''

    tasks = [wait_random(max_delay) for _ in range(n)]
    completed_tasks = await asyncio.gather(*tasks)
    return sorted(completed_tasks)
