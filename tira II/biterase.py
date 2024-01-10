def r(s, d={}):
    if s in d:
        return d[s]
    else:
        d[s] = 0
    if len(s) == 2:
        if s[0] == s[1]:
            d[s] = 1
        return d[s]
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            d[s] += r(s[:i-1]+s[i+1:], d)
    return d[s]

def count(s: str):
    if s.count("1") % 2 == 1 or s.count("0") % 2 == 1:
        return 0
    return r(s)