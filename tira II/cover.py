def find_open(t):
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j] == 0:
                return (i, j)
    return (-1, -1)

def area_size(t, n, m):
    for i in range(m, len(t[n])):
        if t[n][i] == 1:
            return (i-m, len(t)-n)
    return (len(t[n])-m, len(t)-n)

def mark_rectangle(t, n, m, width, height):
    t2 = []
    for l in t:
        t2.append(l.copy())
    for i in range(n, n+height):
        for j in range(m, m+width):
            t2[i][j] = 1
    return t2

def check(table, limit, rectangles):
    n, m = find_open(table)
    if n == -1: return 1
    if rectangles == limit: return 0
    
    width, height = area_size(table, n, m)

    result = 0
    for i in range(height):
        for j in range(width):
            result += check(mark_rectangle(table, n, m, j+1, i+1), limit, rectangles+1)
    return result

def count(n, m, k):
    table = [[0 for i in range(m)] for j in range(n)]
    return check(table, k, 0)

def empty_rect(grid, y, x, height, width):
    for i in range(height):
        for j in range(width):
            if grid[y+i][x+j]:
                return False
    return True

def fill_rect(grid, y, x, height, width, value):
    for i in range(height):
        for j in range(width):
            grid[y+i][x+j] = value

def search(grid, blocks, y, x):
    n, m = len(grid), len(grid[0])
    if y == n:
        return 1
    elif x == m:
        return search(grid, blocks, y+1, 0)
    elif grid[y][x]:
        return search(grid, blocks, y, x+1)
    elif blocks == 0:
        return 0
    else:
        sum = 0
        for i in range(1, n-y+1):
            for j in range(1, m-x+1):
                if empty_rect(grid, y, x, i, j):
                    fill_rect(grid, y, x, i, j, 1)
                    sum += search(grid, blocks-1, y, x+1)
                    fill_rect(grid, y, x, i, j, 0)
        return sum

def count2(n, m, k):
    grid = [[0]*m for _ in range(n)]
    return search(grid, k, 0, 0)

from time import time
t1 = time()
print(count(4,5,20))
t2 = time()
print(count2(4,5,20))
t3 = time()
print(t2-t1, t3-t2)