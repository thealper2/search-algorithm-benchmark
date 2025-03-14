"""
Exponential Search Algorithm Module

This module contains implementation of exponential search algorithm.
Note: This algorithm requires a sorted array as input.
"""

from typing import List, TypeVar

T = TypeVar("T")


def binary_search_bounded(arr: List[T], target: T, left: int, right: int) -> int:
    """
    Helper function for exponential search implementing bounded binary search.

    Args:
        arr: Sorted list to search in
        target: Element to search for
        left: Left boundary index
        right: Right boundary index

    Returns:
        Index of the element if found, -1 otherwise
    """
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def exponential_search(arr: List[T], target: T) -> int:
    """
    Implementation of the exponential search algorithm.

    Exponential search involves two steps:
    1. Find range where element is present by doubling index
    2. Do binary search in found range

    Time complexity: O(log n)
    Space complexity: O(1)

    Args:
        arr: Sorted list to search in
        target: Element to search for

    Returns:
        Index of the element if found, -1 otherwise
    """
    n = len(arr)

    # If array is empty
    if n == 0:
        return -1

    # If target is at first position
    if arr[0] == target:
        return 0

    # Find range for binary search by doubling index
    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    # Call binary search for the found range
    return binary_search_bounded(arr, target, i // 2, min(i, n - 1))
