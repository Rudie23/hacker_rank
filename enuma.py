
matrix = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

values = (row[i] for i, row in enumerate(matrix))
next(values)
