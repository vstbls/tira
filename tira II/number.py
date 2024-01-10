def count(n):
    def r(n, i):
        if n == 0:
            return 1
        result = 0
        for j in range(i, n+1):
            result += r(n-j, j)
        return result
    return r(n, 1)