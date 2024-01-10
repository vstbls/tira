from heapq import heappush, heappop

class Tasks:
    def __init__(self) -> None:
        self.keko = []

    def add(self, name, priority):
        heappush(self.keko, (10**9 - priority, name))

    def next(self):
        return heappop(self.keko)[1]