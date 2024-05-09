#!/usr/bin/env python3
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

    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    dp = [float("inf")] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        for j in range(1, i // 2 + 1):
            operations = dp[j] + 2  # Copy + Paste
            dp[i] = min(dp[i], operations)

    return dp[n] if dp[n] != float("inf") else 0
