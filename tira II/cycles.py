class Cycles:
    def __init__(self,n):
        self.edges = [[] for i in range(n+1)]

    def add_edge(self,a,b):
        self.edges[a].append(b)

    def check(self):
        def search(v):
            if closed[v]:
                return
            if opened[v]:
                cycle[0] = True
                return
            opened[v] = True
            for n in self.edges[v]:
                search(n)
            closed[v] = True
        opened = [False]*len(self.edges)
        closed = [False]*len(self.edges)
        cycle = [False]
        for v in range(len(self.edges)):
            if closed[v]:
                continue
            search(v)
        return cycle[0]