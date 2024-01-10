def find(s):
    subs = {}
    abc = "abcdefghijklmnopqrstuvwxyz"
    for i in abc:
        subs[i] = 0
    for i in abc:
        for j in abc:
            subs[i+j] = 0
    for i in abc:
        for j in abc:
            for k in abc:
                subs[i+j+k] = 0
    subs[s[0]] += 1
    subs[s[1]] += 1
    subs[s[0:2]] += 1
    for i in range(2, len(s)):
        subs[s[i]] += 1
        subs[s[i-1:i+1]] += 1
        subs[s[i-2:i+1]] += 1
    for k, v in subs.items():
        if v == 0:
            return len(k)
    return 4