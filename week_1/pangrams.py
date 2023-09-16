"""
A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a
pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.

Example
s = 'The quick brown fox jumps over the lazy dog'
The string contains all letters in the English alphabet, so return pangram.

Function Description
Complete the function pangrams in the editor below. It should return the string pangram if the input string is a pan-
gram. Otherwise, it should return not pangram.

Input format
A single line with string.

Return sting either pangram or not pangram

    >>> s = 'We promptly judged antique ivory buckles for the prize'
    >>> pangrams(s)
    'not pangram'
    >>> s = 'The quick brown fox jumps over the lazy dog'
    >>> pangrams(s)
    'pangram'
"""
import string


def pangrams(s: str):
    # The function is expected to return a STRING.
    # The function accepts STRING s as parameter.
    if 0 < len(s) <= 10 ** 3:
        alphabet = string.ascii_uppercase
        alphabet_low = alphabet.lower()
        alp_set = set(alphabet_low)

        string_low = s.lower().replace(' ', '')
        string_set = set(string_low)

        res = alp_set - string_set
        if res:
            return 'not pangram'
        else:
            return 'pangram'


pangrams('We promptly judged antique ivory buckles for the prize')
