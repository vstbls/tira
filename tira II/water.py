from heapq import heappop, heappush

def count(a,b,x):
    heap = [(0, (0, 0))]
    visited = set()
    liters = {(0,0): 0}
    while len(heap) > 0:
        v = heappop(heap)[1]
        if v in visited:
            continue
        visited.add(v)
        if v[0] == x:
            return liters[v]
        for op in [
            # fill
            (a-v[0]+liters[v],(a,v[1])),
            (b-v[1]+liters[v],(v[0],b)),
            # empty
            (v[0]+liters[v],(0,v[1])),
            (v[1]+liters[v],(v[0],0)),
            # pass
            (min(v[0], b-v[1])+liters[v],(v[0]-min(v[0], b-v[1]),v[1]+min(v[0], b-v[1]))),
            (min(v[1], a-v[0])+liters[v], (v[0]+min(v[1], a-v[0]),v[1]-min(v[1], a-v[0])))]:
            if op[1] not in liters or liters[v]+op[0] < liters[op[1]]:
                heappush(heap, op)
                liters[op[1]] = op[0]
    return -1