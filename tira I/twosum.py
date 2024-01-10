def rec_find(t: list, x: int, i: int, left: int, right: int):
    if left == right:
        if t[left] + i > x:
            return left-1
        return left
    center = (left+right)//2
    if t[center] + i > x:
        return rec_find(t, x, i, left, center)
    else:
        return rec_find(t, x, i, center + 1, right)

def find(t: list, x: int):
    t = sorted(t)
    total = 0
    for i in range(len(t)-1):
        total += rec_find(t, x, t[i], i+1, len(t) - 1) - i
    return total