from heapq import heappush, heappop

class SameWeight:
    def __init__(self,n):
        self.roads = [[] for _ in range(n+1)]
        self.n = n

    def add_edge(self,a,b,x):
        self.roads[a].append((x,b))
        self.roads[b].append((x,a))

    def min_cost(self):
        visited = [False]*(self.n+1)
        n = 1
        cost = 0
        heap = []
        for i in range(len(self.roads)):
            if len(self.roads[i]) > 0:
                for r in self.roads[i]:
                    heappush(heap, r)
                visited[i] = True
                break
        while len(heap) > 0 and n < self.n:
            road = heappop(heap)
            if not visited[road[1]]:
                visited[road[1]] = True
                cost += road[0]
                n += 1
                for r in self.roads[road[1]]:
                    heappush(heap, r)
        return cost if n == self.n else -1

    def max_cost(self):
        visited = [False]*(self.n+1)
        n = 1
        cost = 0
        heap = []
        for i in range(len(self.roads)):
            if len(self.roads[i]) > 0:
                for r in self.roads[i]:
                    heappush(heap, (1000-r[0], r[1]))
                visited[i] = True
                break
        while len(heap) > 0 and n < self.n:
            road = heappop(heap)
            if not visited[road[1]]:
                visited[road[1]] = True
                cost += 1000 - road[0]
                n += 1
                for r in self.roads[road[1]]:
                    heappush(heap, (1000-r[0], r[1]))
        return cost if n == self.n else -1

    def check(self):
        smallest = self.min_cost()
        largest = self.max_cost()
        return smallest == largest