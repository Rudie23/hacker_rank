"""Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four
of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated
long integers."""
from typing import List


def min_max_sum(arr: List):
    arr_sorted = sorted(arr)
    min_sum = sum(arr_sorted[:-1])
    max_sum = sum(arr_sorted[1:])
    print(min_sum, max_sum)


min_max_sum([1, 3, 5, 7, 7])
