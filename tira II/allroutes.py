class AllRoutes:
    def __init__(self,n):
        self.routes = [[-1]*n for i in range(n)]
        self.n = n
        self.calculated = True
        for i in range(n):
            self.routes[i][i] = 0
 
    def add_road(self,a,b,x):
        a -= 1
        b -= 1
        if self.routes[a][b] == -1:
            self.routes[a][b] = x
        else:
            self.routes[a][b] = min(self.routes[a][b], x)
        self.routes[b][a] = self.routes[a][b]
        self.calculated = False
 
    def get_table(self):
        if not self.calculated:
            for k in range(self.n):
                for i in range(self.n):
                    for j in range(i+1):
                        if self.routes[i][k] == -1 or self.routes[k][j] == -1:
                            continue
                        if self.routes[i][j] == -1:
                            self.routes[i][j] = self.routes[i][k]+self.routes[k][j]
                        else:
                            self.routes[i][j] = min(self.routes[i][j],self.routes[i][k]+self.routes[k][j])
                        self.routes[j][i] = self.routes[i][j]
            self.calculated = True
        return self.routes