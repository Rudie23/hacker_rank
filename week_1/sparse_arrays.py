"""
There is a collection of input strings and a collection of query strings. For each query string, determine how
many times it occurs in the list of input strings. Return an array of the results.

Example:
    strings = ['ab', 'ab', 'abc']
    queries = ['ab', 'abc', 'bc']
Thera are 2 instances of 'ab', 1 of 'abc' and 0 of 'bc' For each query, add an element to return array,
results = [2, 1, 0].

Function Description
Complete the function matchingStrings in the editor below. The function must return an array of integers representing
the frequency of occurrence of each query string in strings.
matchingStrings has the following parameters:

    string strings[n] - an array of strings to search
    string queries[q] - an array of query strings

Returns
    int[q]: an array of results for each query
    >>> strings, queries  = ['ab', 'ab', 'abc'], ['ab', 'abc', 'bc']
    >>> matching_string(strings, queries)
    [2, 1, 0]
"""
from typing import List


def matching_string(strings: List, queries: List):
    count = {}
    for s in strings:
        count[s] = count.get(s, 0) + 1
    return [count.get(query, 0) for query in queries]


x = matching_string(['ab', 'ab', 'abc'], ['ab', 'abc', 'bc'])
print(x)
