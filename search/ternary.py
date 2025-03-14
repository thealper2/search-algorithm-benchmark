"""
Ternary Search Algorithm Module

This module contains implementation of ternary search algorithm.
Note: This algorithm requires a sorted array as input.
"""

from typing import List, TypeVar

T = TypeVar("T")


def ternary_search(arr: List[T], target: T) -> int:
    """
    Implementation of the ternary search algorithm.

    Ternary search divides the array into three parts and determines
    which part to search next.

    Time complexity: O(log3 n)
    Space complexity: O(1)

    Args:
        arr: Sorted list to search in
        target: Element to search for

    Returns:
        Index of the element if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        # Calculate positions of the two mid points
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        # Check if target is at one of the mid points
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        # Determine which part to search next
        if target < arr[mid1]:
            # Search in the first part
            right = mid1 - 1
        elif target > arr[mid2]:
            # Search in the third part
            left = mid2 + 1
        else:
            # Search in the middle part
            left = mid1 + 1
            right = mid2 - 1

    # Element not found
    return -1
