#!/usr/bin/env python3
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension
"""measuring runtime"""


async def measure_runtime():
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
        )
    end_time = time.time() - start_time
    return end_time
