#!/usr/bin/env python3
'''
This function is wait_n rewritten
'''

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List:
    '''Returns a list of delays'''

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed_tasks = await asyncio.gather(*tasks)
    return sorted(completed_tasks)
