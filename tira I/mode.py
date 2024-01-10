class Mode:
    def __init__(self) -> None:
        self.n = {}
        self.mode = (0, 0)
 
    def add(self, x):
        if x not in self.n:
            self.n[x] = 0
        self.n[x] += 1
        n = self.n[x]
        if self.mode[1] < n or (self.mode[1] == n and self.mode[0] > x):
            self.mode = (x, n)
        return self.mode[0]