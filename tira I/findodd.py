import time
from random import shuffle

def find(t):
    n = {}
    for i in t:
        if i not in n:
            n[i] = 0
        n[i] += 1
    for i in n:
        if n[i] == 1:
            return i
            
def find2(t):
    t = sorted(t)
    for i in range(len(t)-1):
        if t[i] != t[i+1] and i % 2 == 0:
            return t[i]
    return t[-1]

if __name__ == "__main__":
    ns = 10000000
    l = [0]*(ns+1)
    for i in range(ns//2):
        l[i*2] = i
        l[i*2+1] = i
    l[ns] = 283740238640923793284
    shuffle(l)
    time1 = time.time()
    print(find(l))
    time2 = time.time()
    print(find2(l))
    time3 = time.time()
    print(time2 - time1, time3 - time2)