from heapq import heappush, heappop

def find(t, k):
    s = sorted(t)
    heap = []
    for i in range(len(s)-1):
        heappush(heap, (s[i+1]-s[i], i, i+1))
    for i in range(k-1):
        _, left, right = heappop(heap)
        if right < len(s)-1:
            heappush(heap, (s[right+1]-s[left], left, right+1))
    return heappop(heap)[0]