"""
Fibonacci Search Algorithm Module

This module contains implementation of fibonacci search algorithm.
Note: This algorithm requires a sorted array as input.
"""

from typing import List, TypeVar

T = TypeVar("T")


def fibonacci_search(arr: List[T], target: T) -> int:
    """
    Implementation of the fibonacci search algorithm.

    Fibonacci search uses Fibonacci numbers to divide the array and search.

    Time complexity: O(log n)
    Space complexity: O(1)

    Args:
        arr: Sorted list to search in
        target: Element to search for

    Returns:
        Index of the element if found, -1 otherwise
    """
    n = len(arr)

    # Initialize Fibonacci numbers
    fib2 = 0  # (n-2)'th Fibonacci number
    fib1 = 1  # (n-1)'th Fibonacci number
    fib = fib1 + fib2  # n'th Fibonacci number

    # Find the smallest Fibonacci number greater than or equal to n
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    # Offset for the eliminated range
    offset = -1

    # While there are elements to be inspected
    while fib > 1:
        # Check if fib2 is a valid index
        i = min(offset + fib2, n - 1)

        # If target is greater than the value at index i,
        # cut the subarray from offset to i
        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        # If target is less than the value at index i,
        # cut the subarray after i+1
        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        # Element found
        else:
            return i

    # Compare the last element
    if fib1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1

    # Element not found
    return -1
