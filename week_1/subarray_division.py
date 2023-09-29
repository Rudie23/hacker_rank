"""
Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.
Lily decides to share a contiguous segment of the bar selected such that:
    .The length of the segment matches Ron's birth month, and
    .The sum of the integers on the squares is equal to his birthday.
Determine how many ways she can divide the chocolate.

Example
    s = [2, 2, 1, 3, 2]
    d = 4
    m = 2
Lily wants to find segments summing to Ron's birthday, d=4 with a length equaling his birth month, m=2.
In this case, there are two segments meeting her criteria: [2, 2] and [1, 3].

Function Description
Complete the birthday function in the editor below.

birthday has the following parameter(s):

    .int s[n]: the numbers on each of the squares of chocolate
    .int d: Ron's birthday
    .int m: Ron's birth month

Returns
    .int: the number of ways the bar can be divided

    >>> arr1, month1, day1 = [2, 2, 2, 3, 1], 2, 4
    >>> print(birthday(s=arr1, d=day1, m=month1))
    3
    >>> arr2, month2, day2 = [4], 1, 4
    >>> print(birthday(s=arr2, d=day2, m=month2))
    1
"""
from typing import List

arr = [2, 2, 1, 3, 2]
birth_month = 2
birth_day = 4


def birthday(s: List, d: int, m: int) -> int:
    # Write your code here

    bar_chocolate = list()
    chocolate = s.copy()

    if len(chocolate) == 1:
        if sum(chocolate) == d:
            return len(chocolate)
    else:
        for idx, _ in enumerate(chocolate):
            lista = chocolate[idx:idx + m]
            if len(lista) == 1:
                break
            bar_chocolate.append(lista)

    bars = [sum(bars) for _, bars in enumerate(bar_chocolate) if sum(bars) == d]

    return len(bars)


if __name__ == '__main__':
    print(birthday(s=arr, d=birth_day, m=birth_month))
