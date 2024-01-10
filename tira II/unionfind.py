from random import randrange
from time import time

def union_find(n):
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    
    parent = list(range(n))
    members = [0]*n
    components = n
    for i in range(n):
        a = find(randrange(n))
        b = find(randrange(n))
        if a == b:
            continue
        if members[a] > members[b]:
            a,b = b,a
        parent[a] = b
        members[b] += members[a]
        components -= 1
    return components

if __name__ == "__main__":
    t = [time()]
    components = []
    for i in range(2,6):
        components.append(union_find(10**i))
        t.append(time())
    #union_find(100)
    #t.append(time())
    #union_find(1000)
    #t.append(time())
    #union_find(10000)
    #t.append(time())
    #union_find(100000)
    #t.append(time())
    print("\n".join([f"Time {t[i+1]-t[i]}s, {components[i]} components" for i in range(len(t)-1)]))