"""
Given an array of integers, where all elements but one occur twice, find the unique element.
Example:
    a = [1,2,3,4,3,2,1]
    The unique element is 4

Function Description

Complete the lonelyinteger function in the editor below. Lonelyinteger has the following parameter(s):

    int a[n]: an array of integers

Returns

    int: the element that occurs only once

    >>> lonely_integer([1, 2, 3, 4, 3, 2, 1])
    4
    >>> lonely_integer([1, 1, 2, 2, 6, 6, 7])
    7
"""
from typing import List


def lonely_integer(arr: List) -> int:
    lista = dict()
    for number in arr:
        lista[number] = lista.get(number, 0) + 1

    for i in lista:
        if lista[i] == 1:
            return i


print(lonely_integer([1, 2, 3, 4, 3, 2, 1]))
