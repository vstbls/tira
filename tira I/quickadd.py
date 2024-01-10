from heapq import heappush, heappop

class QuickAdd:
    def __init__(self) -> None:
        self.keko = []
    
    def add(self, k, x):
        heappush(self.keko, (x, k))

    def remove(self, k):
        counter = 0
        removed = []
        while counter < k:
            removed.append(heappop(self.keko))
            counter += removed[-1][1]
        diff = counter - k
        sums = [i[0] * i[1] for i in removed[:-1]]
        sums.append(removed[-1][0]*(removed[-1][1]-diff))
        if diff > 0:
            heappush(self.keko, (removed[-1][0], diff))
        return sum(sums)