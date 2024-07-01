#!/usr/bin/python3
"""
This is the '0-prime_game' module
"""


def isWinner(x, nums):
    """
    Determines the winner of the game
    """
    if not nums or x < 1:
        return None
    n = max(nums)
    primes = [True for _ in range(max(n + 1, 2))]
    primes[0], primes[1] = False, False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    primes = [i for i, p in enumerate(primes) if p]
    wins = [0, 0]
    for _ in range(x):
        for n in nums:
            if n < 2:
                wins[1] += 1
            elif sum((p <= n for p in primes)) % 2 == 0:
                wins[1] += 1
            else:
                wins[0] += 1
    if wins[0] > wins[1]:
        return "Maria"
    if wins[0] < wins[1]:
        return "Ben"
    return None
