"""
Linear Search Algorithms Module

This module contains implementations of linear search algorithms.
"""

from typing import List, TypeVar

T = TypeVar("T")


def linear_search(arr: List[T], target: T) -> int:
    """
    Implementation of the standard linear search algorithm.

    Time complexity: O(n)
    Space complexity: O(1)

    Args:
        arr: List to search in
        target: Element to search for

    Returns:
        Index of the element if found, -1 otherwise
    """
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1


def sentinel_linear_search(arr: List[T], target: T) -> int:
    """
    Implementation of sentinel linear search algorithm.

    This algorithm eliminates the need for the boundary check in each iteration
    by placing a sentinel (the target) at the end of the array.

    Time complexity: O(n)
    Space complexity: O(1) - Note that we create a copy, but this is still constant
                           relative to the algorithm's operation

    Args:
        arr: List to search in
        target: Element to search for

    Returns:
        Index of the element if found, -1 otherwise
    """
    # Create a copy to avoid modifying the original array
    temp_arr = arr.copy()

    # Length of the original array
    length = len(temp_arr)

    # Add the target element at the end
    temp_arr.append(target)

    i = 0
    while temp_arr[i] != target:
        i += 1

    # If i is less than the original length, we found the element
    # Otherwise, the element was not in the original array
    if i < length:
        return i
    else:
        return -1
