

def arithmetic_progression_sum(a, n, r):
    s = ((a + (a + (n - 1) * r)) * n) // 2
    print(s)


arithmetic_progression_sum(0, 100_000_000, 1)


def arithmetic_progression_term(a, n, r):
    t = a + (n - 1) * r
    print(t)


arithmetic_progression_term(1, 100_000_000, 1)
