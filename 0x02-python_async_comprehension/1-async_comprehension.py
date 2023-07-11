#!/usr/bin/env python3
import random
import asyncio
async_generator = __import__('0-async_generator').async_generator
"""async generator"""


async def async_comprehension():
    """async generator"""
    async_numbers = [number async for number in async_generator()]
    return async_numbers
