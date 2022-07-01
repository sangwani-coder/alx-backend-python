#!/usr/bin/env python3
""" measure runtime """
import asyncio
from timeit import default_timer
import random

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ executes comprehesion coroutine 4 times in parallel
        measure and return the total runtime
    """
    start = default_timer()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    end = default_timer()
    return end - start
