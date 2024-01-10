from collections import deque

def count(r):
    def find(c):
        for y in range(h):
            for x in range(w):
                if r[y][x] == c:
                    return (y,x)

    w = len(r[0])
    h = len(r)
    visited = [[False]*w for i in range(h)]
    dist = [[0]*w for i in range(h)]
    for i in range(h):
        for j in range(w):
            visited[i][j] = r[i][j] == "#"
    y,x = find("A")

    q = deque()
    dist[y][x] = 0
    q.append((y,x))
    while len(q) != 0:
        v = q.popleft()
        d = dist[v[0]][v[1]]+1
        if r[v[0]][v[1]] == "B":
            return d-1
        if not visited[v[0]-1][v[1]]:
            q.append((v[0]-1,v[1]))
            visited[v[0]-1][v[1]] = True
            dist[v[0]-1][v[1]] = d
        if not visited[v[0]][v[1]-1]:
            q.append((v[0],v[1]-1))
            visited[v[0]][v[1]-1] = True
            dist[v[0]][v[1]-1] = d
        if not visited[v[0]+1][v[1]]:
            q.append((v[0]+1,v[1]))
            visited[v[0]+1][v[1]] = True
            dist[v[0]+1][v[1]] = d
        if not visited[v[0]][v[1]+1]:
            q.append((v[0],v[1]+1))
            visited[v[0]][v[1]+1] = True
            dist[v[0]][v[1]+1] = d
    return -1