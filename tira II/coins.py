def count(t):
    s = sum(t)
    t.sort()
    summat = [False]*s
    summat[0] = True
    for i in range(len(t)):
        for j in range(s-1, -1, -1):
            if summat[j]:
                try:
                    summat[j+t[i]] = True
                except:
                    pass
    return sum(summat)