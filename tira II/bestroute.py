from heapq import heappush, heappop

class BestRoute:
    def __init__(self,n):
        self.routes = [[] for i in range(n)]
        self.n = n

    def add_road(self,a,b,x):
        a -= 1
        b -= 1
        self.routes[a].append((b,x))
        self.routes[b].append((a,x))

    def find_route(self,a,b):
        a -= 1
        b -= 1

        keko = []
        kasitelty = [False]*self.n
        dist = [-1]*self.n
        heappush(keko, (0,a))
        while len(keko) > 0:
            solmu = heappop(keko)[1]
            if kasitelty[solmu]:
                continue
            kasitelty[solmu] = True
            for edge in self.routes[solmu]:
                nyky = dist[edge[0]]
                uusi = dist[solmu]+edge[1]
                if uusi < nyky or nyky == -1:
                    dist[edge[0]] = uusi
                    heappush(keko, (uusi, edge[0]))
        result = dist[b]
        if result == -1:
            return -1
        return result+1

    
if __name__ == "__main__":
    b = BestRoute(3)
    b.add_road(1,2,2)
    print(b.find_route(1,3)) # -1
    b.add_road(1,3,5)
    print(b.find_route(1,3)) # 5
    b.add_road(2,3,1)
    print(b.find_route(1,3)) # 3