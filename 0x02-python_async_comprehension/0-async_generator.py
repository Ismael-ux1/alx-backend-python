#!/usr/bin/env python3
""" Asyncronous generator that yields a random number between 0 and 1- """
import asyncio
import random


async def async_generator():
    """
    Asyncronous generator that yields a random number between 0 and 10

    Yields:
    - int: A random number between 0 and 10
    """
    for _ in range(10):
        # Asyncronously wait for 1 second
        await asyncio.sleep(1)
        # Using uniform for floating-point number
        yield random.uniform(0, 10)
