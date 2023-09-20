"""
    >>> arr = [1, 2, 3, 4, 5]
    >>> print(reverse_array(arr))
    [5, 4, 3, 2, 1]
"""

from typing import List


def reverse_array(arr: List) -> List:
    return arr[::-1]
