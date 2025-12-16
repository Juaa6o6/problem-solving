T = int(input())

for tc in range(1, T+1):
    m = int(input())
    n = 0

    grid = [[0]*m for _ in range(m)]
    visited = [[0]*m for _ in range(m)]

    dry = [0, 1, 0, -1]
    drx = [1, 0, -1, 0]

    y = 0
    x = 0
    for _ in range(m):
        for d in range(4):
            ty, tx = y, x
            for i in range(m):
                dy = i * dry[d] + ty
                dx = i * drx[d] + tx
                if dy<0 or dx<0 or dy>m-1 or dx>m-1: continue
                if visited[dy][dx] == 0:
                    n += 1
                    grid[dy][dx] = n
                    visited[dy][dx] = 1
                    y, x = dy, dx

    print(f'#{tc}')
    for i in range(m):
        for j in range(m):
            print(grid[i][j], end=' ')
        print()
