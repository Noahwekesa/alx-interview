#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to achieve n H characters.

    Args:
        n: The desired number of H characters.

    Returns:
        The fewest number of operations needed, or 0 if n is impossible.
    """
    if n <= 1:
        return 0
    operations = 0
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            n /= divisor
            operations += divisor
        else:
            divisor += 1
    return operations
