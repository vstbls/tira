from collections import deque

class FlipList:
    def __init__(self) -> None:
        self.list = deque()
        self.flipped = False

    def push_last(self,x):
        if self.flipped:
            return self.list.appendleft(x)
        return self.list.append(x)

    def push_first(self,x):
        if self.flipped:
            return self.list.append(x)
        return self.list.appendleft(x)

    def pop_last(self):
        if self.flipped:
            return self.list.popleft()
        return self.list.pop()

    def pop_first(self):
        if self.flipped:
            return self.list.pop()
        return self.list.popleft()

    def flip(self):
        self.flipped = not self.flipped