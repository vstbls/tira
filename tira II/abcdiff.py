def create(n):
    letters = ['A', 'B', 'C']
    strs = []
    def recursion(s):
        if len(s)-1 == n:
            return strs.append(s[1:])
        for c in letters:
            if s[-1] != c:
                recursion(s+c)
    recursion(' ')
    return strs