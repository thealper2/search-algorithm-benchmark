"""
Interpolation Search Algorithm Module

This module contains implementation of interpolation search algorithm.
Note: This algorithm requires a sorted array as input and works best
on uniformly distributed data.
"""

from typing import List, TypeVar, Union

T = TypeVar("T")


def interpolation_search(
    arr: List[Union[int, float]], target: Union[int, float]
) -> int:
    """
    Implementation of the interpolation search algorithm.

    Interpolation search estimates the position of the target based on its value
    and the values at the bounds of the search space.

    Time complexity: O(log log n) for uniformly distributed data, O(n) in worst case
    Space complexity: O(1)

    Args:
        arr: Sorted list of numbers to search in
        target: Number to search for

    Returns:
        Index of the element if found, -1 otherwise
    """
    # Handle edge cases
    n = len(arr)
    if n == 0:
        return -1

    low, high = 0, n - 1

    while low <= high and arr[low] <= target <= arr[high]:
        # Check for division by zero
        if arr[high] == arr[low]:  # If all elements are the same
            if arr[low] == target:
                return low
            else:
                return -1

        # Formula for interpolation search
        # Calculate position with floating-point arithmetic
        try:
            pos = low + int(
                ((float(high - low) / (arr[high] - arr[low])) * (target - arr[low]))
            )
        except (TypeError, ValueError):
            # If we can't do the calculation (non-numeric types), fall back to binary search
            pos = low + (high - low) // 2

        # Ensure pos is within bounds
        pos = max(low, min(pos, high))

        # Check if target is found
        if arr[pos] == target:
            return pos

        # If target is larger, target is in upper part
        if arr[pos] < target:
            low = pos + 1
        # If target is smaller, target is in lower part
        else:
            high = pos - 1

    # Element not found
    return -1
