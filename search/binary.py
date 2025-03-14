"""
Binary Search Algorithms Module

This module contains implementations of binary search algorithms.
Note: All these algorithms require a sorted array as input.
"""

from typing import List, TypeVar

T = TypeVar("T")


def binary_search(arr: List[T], target: T) -> int:
    """
    Implementation of the standard binary search algorithm.

    Time complexity: O(log n)
    Space complexity: O(1)

    Args:
        arr: Sorted list to search in
        target: Element to search for

    Returns:
        Index of the element if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid

        # If target is greater, ignore left half
        if arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # Element not present
    return -1


def meta_binary_search(arr: List[T], target: T) -> int:
    """
    Implementation of meta binary search (one-sided binary search).

    This algorithm maintains only one bound (right) and computes the optimal
    step size based on this bound.

    Time complexity: O(log n)
    Space complexity: O(1)

    Args:
        arr: Sorted list to search in
        target: Element to search for

    Returns:
        Index of the element if found, -1 otherwise
    """
    if not arr:
        return -1

    length = len(arr)
    # Initialize power of 2 less than or equal to n
    power = 1
    while power < length:
        power *= 2

    # Initialize bound
    bound = 0

    # Search for the bound such that arr[bound] <= target < arr[bound+1]
    while power > 0:
        if bound + power < length and arr[bound + power] <= target:
            bound += power
        power //= 2

    # Check if target is present at bound
    if bound < length and arr[bound] == target:
        return bound

    return -1


def ubiquitous_binary(arr: List[T], target: T) -> int:
    """
    Implementation of ubiquitous binary search (uses binary search
    with a guard for empty arrays).

    Time complexity: O(log n)
    Space complexity: O(1)

    Args:
        arr: Sorted list to search in
        target: Element to search for

    Returns:
        Index of the element if found, -1 otherwise
    """
    if not arr:
        return -1

    left, right = 0, len(arr) - 1

    # First, check if the target is outside the range of the array
    if target < arr[left] or target > arr[right]:
        return -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
