class GraphGame:
    def __init__(self,n):
        self.edges = [[] for _ in range(n+1)]
        self.parents = [[] for _ in range(n+1)]
        self.win = [False]*(n+1)
        self.n = n

    def add_link(self,a,b):
        self.edges[a].append(b)
        self.parents[b].append(a)
        self.parents[b].sort(reverse=True)
        for e in self.edges[a]:
            if not self.win[e]:
                self.win[a] = True
                self.propagate(a)
                break
    
    def propagate(self,x):
        for p in self.parents[x]:
            w = False
            for e in self.edges[p]:
                if not self.win[e]:
                    w = True
            if w != self.win[p]:
                self.win[p] = w
                self.propagate(p)

    def winning(self,x):
        return self.win[x]