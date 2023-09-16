"""
You will be given a list of 32-bit unsigned integers. Flip all the bits (1 -> 0 and 0 -> 1) and return the result as an
unsigned integer.

Function Description
Complete the flippingBits function in the editor below.
flippingBits has the following parameter(s):

    int n: an integer
    len(n) = 10

Input Format
    The first line of the input contains q, the number of queries.
    Each of the next q lines contain an integer, n, to process.

Returns
    int: the unsigned decimal integer result

    >>> flipping_bits(1)
    4294967294
    >>> flipping_bits(2147483647)
    2147483648
    >>> flipping(2147483647)
    2147483648
    >>> flipping(1)
    4294967294
"""


def flipping_bits(n: int) -> int:
    # The function is expected to return a LONG_INTEGER.
    # The function accepts LONG_INTEGER n as parameter.
    bits = f'{n:032b}'
    inverse_bits = ''
    for bit in bits:
        if bit == '0':
            inverse_bits += '1'
        else:
            inverse_bits += '0'
    number = int(inverse_bits, 2)
    return number


# By Hackers Realm
def flipping(n: int) -> int:
    return 2 ** 32 + ~n
