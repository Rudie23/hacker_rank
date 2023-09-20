"""
    >>> print(max_min([1,2,3,4,5]))
    (5, 1)
    >>> print(type(max_min([1,2,3,4,5])))
    <class 'tuple'>
"""

from typing import List


def max_min(lst: List):
    """
    :param lst
    :return: tuple
    """
    max_value = min_value = lst[0]
    for value in lst:
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value

    return max_value, min_value
