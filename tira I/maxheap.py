def count(n):
    summa = 0
    i = 1
    while(2**i-1 <= n):
        summa += 2**(i-1)*(i-1)
        i += 1
    summa += (n-(2**(i-1)-1))*(i-1)
    return summa