#!/usr/bin/env python3
"""
calculate the factorial of a number using recursion
"""


def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= 1
    return fact


print(factorial(5))
