# Grid with calculated n.o. moves
# BFS box -> exit
# On every step check if box is movable and if robot can reach the box
# BFS robot to box
# Add robot's distance to counter
# If counter less than n.o. moves in spot pushed to, write it there
# Try with a dict idk

from collections import deque

def count(r):
    def find(c):
        for y in range(len(r)):
            for x in range(len(r[0])):
                if r[y][x] == c:
                    return (y,x)
    def x_path(y,x,xy,xx,dy,dx):
        if xy == y-dy and xx == x-dx:
            return 0
        w = len(r[0])
        h = len(r)
        jono = deque()
        jono.append((xy,xx))
        visited = [[False]*w for i in range(h)]
        distance = [[0]*w for i in range(h)]
        visited[xy][xx] = True
        while len(jono) > 0:
            vy,vx = jono.popleft()
            for ddy,ddx in dirs:
                if vy+ddy == y-dy and vx+ddx == x-dx:
                    return distance[vy][vx]+1
                if distance[vy+ddy][vx+ddx] != 0 or r[vy+ddy][vx+ddx] == "#" or (vy+ddy == y and vx + ddx == x):
                    continue
                jono.append((vy+ddy,vx+ddx))
                visited[vy+ddy][vx+ddx] = True
                distance[vy+ddy][vx+ddx] = distance[vy][vx]+1
        return -1
    w = len(r[0])
    h = len(r)
    q = deque()
    y,x = find("B")
    xy,xx = find("X")
    yy,yx = find("Y")
    q.append((y,x,xy,xx,0))
    moves = [[999]*w for i in range(h)]
    moves[y][x] = 0
    pos = {}
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    result = -1
    while len(q) > 0:
        y,x,xy,xx,m = q.popleft()
        if y == yy and x == yx:
            if result == -1:
                result = moves[y][x]
            else:
                result = min(moves[y][x],result)
        for dy,dx in dirs:
            if r[y+dy][x+dx] != "#" and r[y-dy][x-dx] != "#":
                dist = x_path(y,x,xy,xx,dy,dx)
                m2 = m+dist+1
                ind = (y+dy,x+dx,y,x)
                if ind not in pos:
                    pos[ind] = 999
                if dist != -1 and pos[ind] > m2:
                    pos[ind] = m2
                    moves[y+dy][x+dx] = min(m2,moves[y+dy][x+dx])
                    q.append((y+dy,x+dx,y,x,m2))
    return result