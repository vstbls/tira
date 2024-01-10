def count(s):
    result = 0
    chars = {}
    for c in s:
        if c in chars:
            chars[c] += 1
        else: chars[c] = 1
        result += chars[c]
    return result