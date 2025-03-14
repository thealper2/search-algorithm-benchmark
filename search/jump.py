"""
Jump Search Algorithm Module

This module contains implementation of jump search algorithm.
Note: This algorithm requires a sorted array as input.
"""

import math
from typing import List, TypeVar

T = TypeVar("T")


def jump_search(arr: List[T], target: T) -> int:
    """
    Implementation of the jump search algorithm.

    Jump search works by jumping ahead by fixed steps and then doing a linear
    search once we've found a range where the target might exist.

    Time complexity: O(sqrt(n))
    Space complexity: O(1)

    Args:
        arr: Sorted list to search in
        target: Element to search for

    Returns:
        Index of the element if found, -1 otherwise
    """
    n = len(arr)

    # Finding optimal jump step size: sqrt(n)
    step = int(math.sqrt(n))

    # Finding the block where the element might be present
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Doing a linear search in the identified block
    while arr[prev] < target:
        prev += 1

        # If we reach the end of the block or the end of the array
        if prev == min(step, n):
            return -1

    # Check if element is found
    if arr[prev] == target:
        return prev

    return -1
