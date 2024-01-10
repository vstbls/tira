from collections import deque

def solve(n,k):
    l = deque([i for i in range(1,n+1)])
    for i in range(k):
        l.append(l[1])
        l.append(l[0])
        l.popleft()
        l.popleft()
    return l[0]