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
"""
from typing import List

lista = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]


def diagonal(arr: List) -> int:
    # Here it is the code
    size = len(arr)
    left_to_right = []
    right_to_left = []
    for i in range(0, 1):
        for j in range(0, size):
            if j > size:
                break

            left_to_right.append(arr[i][j])
            i = i + 1

        if i == size:
            i = 0

        for j in range(size - 1, -1, -1):

            right_to_left.append(arr[i][j])
            i += 1

    sum_lists = abs(sum(left_to_right) - sum(right_to_left))
    return sum_lists


diagonal(lista)
