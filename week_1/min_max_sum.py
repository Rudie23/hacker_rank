"""Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four
of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated
long integers."""
from math import inf
from typing import List


def min_max_sum(arr: List):
    min_value = inf
    max_value = -inf
    for value in arr:
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value
    arr1 = arr.copy()
    arr2 = arr.copy()

    for _ in arr1:
        if min_value in arr1:
            arr1.remove(min_value)
        else:
            continue

    for _ in arr2:
        if max_value in arr2:
            arr2.remove(max_value)
        else:
            continue

    print(sum(arr2), sum(arr1))


min_max_sum([1, 3, 5, 7, 9])
