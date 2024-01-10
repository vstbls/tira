def count(n: int):
    total = 0
    for i in range(n):
        for j in range(n):
            board = [[1 for w in range(n)] for q in range(n)]
            def zero(x: int, y: int):
                if (0 <= x < n) and (0 <= y < n):
                    board[x][y] = 0
            zero(i, j)
            for k in range(1, n):
                zero(i-k, j-k)
                zero(i-k, j)
                zero(i-k, j+k)
                zero(i, j-k)
                zero(i, j+k)
                zero(i+k, j-k)
                zero(i+k, j)
                zero(i+k, j+k)
            zero(i-2, j-1)
            zero(i-2, j+1)
            zero(i+2, j-1)
            zero(i+2, j+1)
            zero(i-1, j-2)
            zero(i+1, j-2)
            zero(i-1, j+2)
            zero(i+1, j+2)
            total += sum([sum(row) for row in board])
    return total