def count(n: int):
    total = 0
    for i in range(2, n + 1):
        fail = False
        for j in range(2, i):
            if i % j == 0:
                fail = True
        if not fail:
            total += 1
    return total