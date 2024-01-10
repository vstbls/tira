class LongPath:
    def __init__(self,n):
        self.n = n
        self.verts = [[] for _ in range(n+1)]

    def add_edge(self,a,b):
        self.verts[a].append(b)
        self.verts[b].append(a)

    def calculate(self):
        self.dists = [0]*(self.n+1)
        for v in range(1, self.n+1):
            for e in self.verts[v]:
                if e >= v:
                    continue
                self.dists[v] = max(self.dists[e]+1, self.dists[v])
        return max(self.dists)