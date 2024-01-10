def count(n,a,b):
    askeleet = [0]*(n+1)
    askeleet[a] = 1
    askeleet[b] = 1
    for i in range(a+1, n+1):
        a_askel = 0
        b_askel = 0
        if i-a >= 0: a_askel = askeleet[i-a]
        if i-b >= 0: b_askel = askeleet[i-b]
        askeleet[i] += a_askel + b_askel
    return askeleet[-1]