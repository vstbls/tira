class MaxSet:
    def __init__(self,n):
        self.n = n
        self.max = 1
        self.set = [(i, 1) for i in range(n+1)]

    def master(self, i):
        while self.set[i][0] != i:
            i = self.set[i][0]
        return i

    def merge(self,a,b):
        a = self.master(a)
        b = self.master(b)
        if a == b:
            return
        if self.set[a][1] > self.set[b][1]:
            a,b = b,a
        self.set[a] = (b, self.set[a][1])
        self.set[b] = (b, self.set[a][1]+self.set[b][1])
        self.max = max(self.set[b][1], self.max)

    def get_max(self):
        return self.max