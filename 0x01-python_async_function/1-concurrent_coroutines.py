#!/usr/bin/env python3
""" defines a routine wait_n that takes in 2
    int arguments (in this order): n and max_delay
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """ Spawns wait_random n times with specified max_delay
        return: A list of all delays(floats) in ascending order.
    """
    res_list = []
    sorted_list = []
    for i in range(n):
        res = await wait_random(max_delay)
        res_list.append(res)
    # Sort the list in ascending order.
    while res_list:
        MIN = res_list[0]
        for x in res_list:
            if x < MIN:
                MIN = x
        sorted_list.append(MIN)
        res_list.remove(MIN)
    return sorted_list
