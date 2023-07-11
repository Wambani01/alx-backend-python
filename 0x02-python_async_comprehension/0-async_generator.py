#!/usr/bin/env python3
import asyncio
import random
"""asynch generator"""


async def async_generator():
    """asynch generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
