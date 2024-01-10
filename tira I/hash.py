def hajauta(s: str):
    A = 17
    z = ord(s[0])
    for c in s[1:]:
        z = A*z + ord(c)
    return z % 997163

while 1:
    print(hajauta(input()))