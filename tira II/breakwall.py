from heapq import heappop, heappush

def count(r):
    def find(c):
        for y in range(len(r)):
            for x in range(len(r[0])):
                if c == r[y][x]:
                    return (y,x)
    start = find("A")
    end = find("B")
    visited = set()
    walls = [[999]*len(r[0]) for i in range(len(r))]
    walls[start[0]][start[1]] = 0
    heap = [(0,start)]
    while len(heap) > 0:
        v = heappop(heap)[1]
        if v in visited:
            continue
        visited.add(v)
        for d in [(-1,0),(1,0),(0,-1),(0,1)]:
            if r[v[0]+d[0]][v[1]+d[1]] == "#":
                continue
            prev = walls[v[0]+d[0]][v[1]+d[1]]
            new = walls[v[0]][v[1]]
            if r[v[0]+d[0]][v[1]+d[1]] == "*":
                new += 1
            if new < prev:
                walls[v[0]+d[0]][v[1]+d[1]] = new
                heappush(heap, (new, (v[0]+d[0],v[1]+d[1])))
    return walls[end[0]][end[1]]