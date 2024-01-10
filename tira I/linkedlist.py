from time import time

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self) -> None:
        self.first = None
        self.last = None
    def append(self, data):
        new = Node(data)
        if self.first is None:
            self.first = new
            self.last = new
            return
        self.last.next = new
        self.last = new
    def pop_first(self):
        if self.first is not None:
            self.first = self.first.next

if __name__ == "__main__":
    l = LinkedList()
    n = 10**5
    t1 = time()
    for i in range(n):
        l.append(i+1)
    t2 = time()
    for i in range(n):
        l.pop_first()
    t3 = time()
    print(t2-t1, t3-t2)
