#!/usr/bin/env python3
""" defines a routine wait_n that takes in 2
    int arguments (in this order): n and max_delay
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, delay: int) -> float:
    """ Spwans wait_random n times with specified max_delay
        return: A list of all delays(floats) in ascending order.
    """
    res_list = []
    for i in range(n):
        res = await wait_random(delay)
        res_list.append(res)
    return res_list
