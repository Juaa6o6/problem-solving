import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    m = int(input())

    # 1. visited 배열 제거, grid만 사용
    grid = [[0] * m for _ in range(m)]

    # 우, 하, 좌, 상 순서 (시계 방향)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r, c = 0, 0  # 현재 좌표 (row, column)
    d = 0  # 현재 방향 인덱스 (0:우, 1:하, 2:좌, 3:상)

    for num in range(1, m * m + 1):
        grid[r][c] = num

        # 다음 위치 계산
        nr, nc = r + dr[d], c + dc[d]

        # 2. 다음 위치가 범위를 벗어나거나, 이미 숫자가 채워진 경우 방향 전환
        if nr < 0 or nr >= m or nc < 0 or nc >= m or grid[nr][nc] != 0:
            d = (d + 1) % 4  # 방향 전환 (0->1->2->3->0)
            nr, nc = r + dr[d], c + dc[d]  # 전환된 방향으로 재설정

        r, c = nr, nc

    print(f'#{tc}')
    for row in grid:
        print(*row)