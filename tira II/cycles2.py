class Cycles:
    def __init__(self,n):
        self.n = n
        self.graph = [[] for _ in range(n+1)]
 
    def add_edge(self,a,b):
        self.graph[a].append(b)
 
    def dfs(self,x):
        if self.color[x] == 1:
            self.found = True
            return
        if self.color[x] == 2:
            return
        self.color[x] = 1
        for y in self.graph[x]:
            self.dfs(y)
        self.color[x] = 2
        self.topo.append(x)
 
    def check(self):
        self.topo = []
        self.color = [0]*(self.n+1)
        self.found = False
        for x in range(1,self.n+1):
            if self.color[x] == 0:
                self.dfs(x)
        self.topo.reverse()
        return self.topo

if __name__ == "__main__":
    c = Cycles(10)
    
    c.add_edge(1,3)
    c.add_edge(1,5)
    
    c.add_edge(2,1)
    c.add_edge(2,5)
    c.add_edge(2,6)

    c.add_edge(3,5)
    c.add_edge(3,7)
    c.add_edge(3,10)

    c.add_edge(4,3)
    c.add_edge(4,6)
    c.add_edge(4,7)

    c.add_edge(5,8)
    c.add_edge(5,9)

    c.add_edge(6,5)
    c.add_edge(6,9)

    c.add_edge(7,6)
    c.add_edge(7,8)
    c.add_edge(7,10)

    c.add_edge(8,9)

    print(c.check())