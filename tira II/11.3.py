n = 4
routes = [
    [0, 5, -1, 15],
    [2, 0, 3, 9],
    [15, 10, 0, 3],
    [-1, 5, -1, 0]
]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if routes[i][k] == -1 or routes[k][j] == -1:
                continue
            if routes[i][j] == -1:
                routes[i][j] = routes[i][k]+routes[k][j]
            else:
                routes[i][j] = min(routes[i][j],routes[i][k]+routes[k][j])
    print(routes)