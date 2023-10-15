"""
There are two n-element arrays of integers, A and B. Permute them into some A' and B' such that relation A'[i] + B'[i]
>= k holds for all i where 0 <= i < n.

There will be q queries consisting of A, B, and k. For each query, return YES if some permutation A', B' satisfying the
relation exists. Otherwise, return NO.

Example
    A = [1, 2]
    B = [0, 2]
    k = 1

    A valid A', B' is A' = [1, 0] and B' = [0, 2]: 1 + 0 >= 1 and 0 + 2 >= 1. Return YES.

Function Description
Complete the twoArrays function in the editor below. It should return a string, either YES or NO.
twoArrays has the following parameter(s):
    .int k: an integer
    .int A[n]: an array of integers
    .int B[n]: an array of integers

Returns
-string: either YES or NO

Sample Input
    STDIN       Function
    -----       --------
    2           q = 2
    3 10        A[] and B[] size n = 3, k = 10
    2 1 3       A = [2, 1, 3]
    7 8 9       B = [7, 8, 9]
    4 5         A[] and B[] size n = 4, k = 5
    1 2 2 1     A = [1, 2, 2, 1]
    3 3 3 4     B = [3, 3, 3, 4]

Sample Output
YES
NO

Explanation

There are two queries:
    1. Permute these into A' = [1, 2, 3] and B' = [9, 8, 7] so that the following satisfying relation are true:
    A'[0] + B'[1] = 1 + 9 = 10 >= K
    A'[1] + B'[1] = 1 + 9 = 10 >= K
    A'[2] + B'[2] = 1 + 9 = 10 >= K
    2. A = [1, 2, 2, 1], B = [3, 3, 3, 4], and k = 5. To permute A and B into a valid A' and B', there must be at least
    three numbers in A that are greater than 1.
"""


def two_arrays(k, A, B):
    A.sort()
    B.sort(reverse=True)

    for x, y in zip(A, B):
        if x + y < k:
            return "NO"
    return "YES"
