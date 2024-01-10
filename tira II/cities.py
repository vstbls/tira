class Cities:
    def __init__(self,n):
        self.cities = [[] for i in range(n+1)]

    def add_road(self,a,b):
        self.cities[a].append(b)
        self.cities[b].append(a)

    def has_route(self,a,b):
        def search(city, dest):
            if visited[city]:
                return
            visited[city] = True
            for c in self.cities[city]:
                search(c, dest)

        visited = [False]*len(self.cities)
        search(a,b)
        return visited[b]