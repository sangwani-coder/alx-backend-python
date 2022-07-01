#!/usr/bin/env python3
""" measure runtime """
import asyncio
import time
import random

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ executes comprehesion coroutine 4 times in parallel
        measure and return the total runtime
    """
    start = time.time()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    end = time.time()
    run_t = end - start
    return run_t
