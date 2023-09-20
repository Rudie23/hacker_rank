"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:
    1 2 3
    4 5 6
    9 8 9
The left-to-right diagonal: 1 + 5 + 9 = 15
The right to left diagonal: 3 + 5 + 9 = 17
absolute difference is |15 - 17| = 2

    >>> test = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    >>> diagonal(test)
    15
    >>> test2 = [[1, 2, 3], [4, 5, 6], [9, 8 , 9]]
    >>> diagonal(test2)
    2
    >>> test3 = [[1, 2, 3], [4, 5, 6], [9, 8 , 9]]
    >>> diagonal_in_pythonic(test2)
    2
"""
from typing import List


def diagonal(matrix: List) -> int:
    # Here it is the code
    left, right = 0, 0
    for ind in range(len(matrix)):
        left += matrix[ind][ind]
        right += matrix[ind][len(matrix) - ind - 1]

    return abs(left - right)


def diagonal_in_pythonic(matrix: List) -> int:
    left = sum(row[i] for i, row in enumerate(matrix))
    right = sum(row[-j - 1] for j, row in enumerate(matrix))
    value_abs = abs(left - right)
    return value_abs
