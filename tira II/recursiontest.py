def recursive_exponent(p: int, n: int):
    def recursion(n: int):
        if n == 0:
            return 1
        return recursion(n-1)*p
    return recursion(n)

print(recursive_exponent(3, 5))