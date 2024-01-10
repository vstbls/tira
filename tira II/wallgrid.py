class WallGrid:
    def __init__(self,n):
        self.n = n
        self.floor = [[False]*(n+1) for _ in range(n+1)]
        self.rooms = 0
        self.parent = {}
        for i in range(n):
            for j in range(n):
                self.parent[(j,i)] = (j,i)

    def find(self,x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def merge(self,a,b):
        self.parent[a] = b
        return b

    def remove(self,x,y):
        if self.floor[y][x]:
            return
        self.floor[y][x] = True
        self.rooms += 1
        parents = set()
        for dir in [(-1,0), (1,0), (0,-1), (0,1)]:
            if self.floor[y+dir[1]][x+dir[0]]:
                p = self.merge(self.find((x,y)), self.find((x+dir[0],y+dir[1])))
                if p not in parents:
                    parents.add(p)
                    self.rooms -= 1

    def count(self):
        return self.rooms