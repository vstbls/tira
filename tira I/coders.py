def find(a,b):
    a_copy = sorted(a)
    b_copy = sorted(b)
    result = 0
    for i in range(len(a)):
        result += abs(a_copy[i]-b_copy[i])
    return result