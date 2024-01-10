def suurin_sama(A: list, B: list):
    s = set(A)
    largest = -1
    for i in B:
        if i in s and i > largest:
            largest = i
    return largest
    