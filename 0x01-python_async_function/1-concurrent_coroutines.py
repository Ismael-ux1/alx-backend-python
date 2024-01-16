#!/usr/bin/env python3
""" Concurrently execute the wait_random coroutine 'n' times. """
import asyncio
import random

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Parameters:
    - n (int): Number of times to execute wait_random.
    - max_delay (int): Maximum delay for each wait_random execution.

    Returns:
    - list: List of delays (float values) in ascending order.
    """
    # Concurrently execute wait_random n times
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

    # Sort the list of delays in ascending order
    delays.sort()

    # Return the sorted list of delays
    return delays
