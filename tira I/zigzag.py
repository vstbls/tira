def create(n: int):
    l = [1]
    for i in range(2, n + 1):
        if i % 2 == 0:
            l.append(i)
        else:
            l.insert(0, i)
    return l