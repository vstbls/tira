def count(s):
    sub_s = '.'
    count = 0
    for c in s:
        if c == sub_s[0]:
            sub_s += c
            count += len(sub_s)
        else:
            sub_s = c
            count += 1
    return count