def dynamic(n):
    if n <= 2:
        return n
    l = [0,1,2]
    for i in range(3, n+1):
        l.append(l[i-1] + l[i-2] + l[i-3])
    return l[-1]

print(dynamic(30))