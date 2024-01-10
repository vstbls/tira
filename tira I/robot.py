def count(s):
    pos = (0,0)
    l = set()
    l.add(pos)
    for c in s:
        if c == "U":
            pos = (pos[0], pos[1]+1)
        if c == "D":
            pos = (pos[0], pos[1]-1)
        if c == "L":
            pos = (pos[0]+1, pos[1])
        if c == "R":
            pos = (pos[0]-1, pos[1])
        l.add(pos)
    return len(l)