#!/usr/bin/python3
"""
pascal triangle function
"""


def pascal_triangle(n):
    """
    This function generates Pascal's triangle up to a given no. of rows

    args:
         n: The no. of rows in the pascal's triangle.
    Returns:
        A list of lists of integers representing the Pascal's triangle

    """
    triangle = []
    if not isinstance(n, int) or n <= 0:
        return triangle
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)
    return triangle
