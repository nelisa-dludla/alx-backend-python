#!/usr/bin/env python3
'''
This is an asynchronous function takes an
integer argument waits for a random delay
between 0 and the argument in seconds, then
returns the random number
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    Waits ofr max_delay in seconds then
    returns a random number
    '''
    random_number = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)

    return random_number
