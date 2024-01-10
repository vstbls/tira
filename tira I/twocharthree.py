def count(s):
    ns = [1,0]
    cs = [s[0]] * 2
    result = 0
    for c in s[1:]:
        if c == cs[0]:
            ns[0] += 1
        else:
            result += ns[0] * ns[1]
            cs.reverse()
            if c in cs:
                ns[1] = sum(ns)
                ns[0] = 1
            else:
                cs[0] = c
                ns.reverse()
                ns[0] = 1
    result += ns[0] * ns[1]
    return result