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
    A = sorted(A)
    B = sorted(B, reverse=True)

    for x, y in zip(A, B):
        if x + y < k:
            return "NO"
    return "YES"


print(two_arrays(5, [1, 2, 2, 1], [3, 3, 3, 4]))

"""
Python zip() with Dictionary

The zip() function in Python is used to combine two or more iterable dictionaries into a single iterable, 
where corresponding elements from the input iterable are paired together as tuples. When using zip() with 
dictionaries, it pairs the keys and values of the dictionaries based on their position in the dictionary."""

stocks = ['GEEKS', 'For', 'geeks']
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks, prices in zip(stocks, prices)}
print(new_dict)
"""
Python zip() with Multiple Iterables

Python’s zip() function can also be used to combine more than two iterables. It can take multiple iterables as input 
and return an iterable of tuples, where each tuple contains elements from the corresponding positions of the input 
iterables."""

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['x', 'y', 'z']
zipped = zip(list1, list2, list3)
result = list(zipped)
print(result)

"""
Python zip() with Tuple

When used with tuples, zip() works by pairing the elements from tuples based on their positions. The resulting 
iterable contains tuples where the i-th tuple contains the i-th element from each input tuple."""

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
zipped = zip(tuple1, tuple2)
result = list(zipped)
print(result)

"""
Unzipping Using zip()

Unzipping means converting the zipped values back to the individual self as they were. This is done with the help of “*”
operator.
"""

# Python code to demonstrate the working of
# unzip

# initializing lists
name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]

# using zip() to map values
mapped = zip(name, roll_no, marks)

# converting values to print as list
mapped = list(mapped)

# printing resultant values
print("The zipped result is : ", end="")
print(mapped)

print("\n")

# unzipping values
namz, roll_noz, marksz = zip(*mapped)

print("The unzipped result: \n", end="")

# printing initial lists
print("The name list is : ", end="")
print(namz)

print("The roll_no list is : ", end="")
print(roll_noz)

print("The marks list is : ", end="")
print(marksz)

"""
Practical Applications

There are many possible applications that can be said to be executed using zip, be it student database or scorecard or
any other utility that requires mapping of groups. A small example of a scorecard is demonstrated below. 
"""

# Python code to demonstrate the application of
# zip()

# initializing list of players.
players = ["Sachin", "Sehwag", "Gambhir", "Dravid", "Raina"]

# initializing their scores
scores = [100, 15, 17, 28, 43]

# printing players and scores.
for pl, sc in zip(players, scores):
    print("Player : %s	 Score : %d" % (pl, sc))
