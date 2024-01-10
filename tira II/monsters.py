def count(r):
    n = len(r[0])
    arvo = {".": 0, "@": 1, "#": 999}
    hirviot = [[0]*(n) for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == 0:
                hirviot[i][j] = arvo[r[i][j]]
                if j != 0:
                    hirviot[i][j] += hirviot[i][j-1]
            elif j == 0:
                hirviot[i][j] = hirviot[i-1][j] + arvo[r[i][j]]
            else:
                hirviot[i][j] = min(hirviot[i-1][j], hirviot[i][j-1]) + arvo[r[i][j]]
    if hirviot[-1][-1] >= 998: return -1
    return hirviot[-1][-1]