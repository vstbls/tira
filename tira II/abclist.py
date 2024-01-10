def create(n):
    letters = ['A', 'B', 'C']
    strs = []
    def recursion(s):
        if len(s) == n:
            return strs.append(s)
        for c in letters:
            recursion(s+c)
    recursion('')
    return strs