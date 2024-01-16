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
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    # Return the sorted list of delays
    return delays
