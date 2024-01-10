class Ball:
    def __init__(self,n):
        self.graph = [[0]*(2*(n+1)) for _ in range(2*(n+1))]
        self.graph[0][1:n+1] = [1]*(n)
        for i in range(n+1, len(self.graph)-1):
            self.graph[i][-1] = 1
        self.n = n

    def add_pair(self,a,b):
        self.graph[a][b+self.n] += 1

    def calculate(self):
        a = 0
        b = len(self.graph)-1
        self.copy = [l.copy() for l in self.graph]
        self.dest = b
        n = self.n
        result = 0
        change = -1
        while change != 0:
            change = 0
            for i in range(1, n+1):
                if self.copy[a][i] != 0:
                    self.visited = [False]*(2*(n+1))
                    flow = self.dfs(i, a, self.copy[a][i])
                    change += flow
            result += change
        return result
            
    def dfs(self,a,b,flow):
        if self.visited[a]:
            return 0
        self.visited[a] = True
        if a == self.dest:
            self.copy[a][b] += flow # child to parent
            self.copy[b][a] -= flow # parent to child
            return flow
        result = 0
        for i in range(0,len(self.graph)):
            if self.copy[a][i] != 0:
                result = self.dfs(i, a, min(flow, self.copy[a][i]))
                if result != 0:
                    self.copy[a][b] += result # child to parent
                    self.copy[b][a] -= result # parent to child
                    return result
        return 0