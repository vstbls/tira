from collections import deque

def count(r):
    def search(y,x):
        q = deque()
        q.append((y,x))
        visited[y][x] = True
        while len(q) != 0:
            v = q.popleft()
            if not visited[v[0]-1][v[1]] and r[v[0]-1][v[1]] == ".":
                q.append((v[0]-1,v[1]))
                visited[v[0]-1][v[1]] = True
            if not visited[v[0]][v[1]-1] and r[v[0]][v[1]-1] == ".":
                q.append((v[0],v[1]-1))
                visited[v[0]][v[1]-1] = True
            if not visited[v[0]+1][v[1]] and r[v[0]+1][v[1]] == ".":
                q.append((v[0]+1,v[1]))
                visited[v[0]+1][v[1]] = True
            if not visited[v[0]][v[1]+1] and r[v[0]][v[1]+1] == ".":
                q.append((v[0],v[1]+1))
                visited[v[0]][v[1]+1] = True

    w = len(r[0])
    h = len(r)
    visited = [[False]*w for i in range(h)]
    for i in range(h):
        for j in range(w):
            visited[i][j] = r[i][j] == "#"
    result = 0
    for y in range(h):
        for x in range(w):
            if not visited[y][x]:
                search(y,x)
                result += 1
    return result