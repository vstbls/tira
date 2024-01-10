def count(s):
    open = 0
    closed = 0
    for c in s:
        if c == "(":
            open += 1
        elif open > 0:
            open -= 1
            closed += 1
    return len(s)-closed*2