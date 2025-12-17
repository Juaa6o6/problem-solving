# import sys
# sys.stdin = open('input.txt', 'r')


def win(i, j):

    hap = 0

    for r in range(m):
        for c in range(m):
            dr = i + r
            dc = j + c
            hap += grid[dr][dc]

    return hap


T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())

    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    Max = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            res = win(i, j)
            Max = max(res, Max)

    print(f'#{tc} {Max}')
