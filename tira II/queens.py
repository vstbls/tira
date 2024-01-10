def count(n):
    n: int = n
    l: list = [0]*n

    def check(y, x):
        for i in range(y):
            if l[i] == x:
                return False
            if abs(i-y) == abs(l[i]-x):
                return False
        return True
    def search(y):
        if y == n:
            return 1
        result = 0
        for x in range(n):
            if check(y, x):
                l[y] = x
                result += search(y+1)
        return result
    return search(0)

for i in range(1,13):
    print(count(i))