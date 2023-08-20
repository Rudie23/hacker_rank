matrix = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

values = (row[-i - 1] for i, row in enumerate(matrix))
for value in values:
    print(value)
