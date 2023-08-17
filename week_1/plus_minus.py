def plus_minus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zer = 0
    for value in arr:
        if value > 0:
            pos = pos + 1
        elif value < 0:
            neg = neg + 1
        elif value == 0:
            zer = zer + 1
    ratio_pos = pos / len(arr)
    ratio_neg = neg / len(arr)
    ratio_zer = zer / len(arr)
    print(f'{ratio_pos:.5f}')
    print(f'{ratio_neg:.5f}')
    print(f'{ratio_zer:.5f}')


plus_minus([1, 2, 3, -1, -2, -3, 0, 0])
