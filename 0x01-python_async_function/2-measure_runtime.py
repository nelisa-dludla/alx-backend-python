#!/usr/bin/env python3
'''
This function measures the approximate
time is takes for wait_n to run
'''

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Returns approximate time of each operation
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return float(total_time/n)
