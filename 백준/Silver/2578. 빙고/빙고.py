bingo = [list(map(int, input().split())) for _ in range(5)]

num = []
for _ in range(5):
    num += list(map(int, input().split()))

def find_num(obj):
    for i in range(5):
        for j in range(5):
            if obj == bingo[i][j]:
                return i, j
    return -1, -1

def check_rc():
    bingo_cnt = 0
    
    # 가로줄 체크 - 수정된 로직
    for i in range(5):
        if all(bingo[i][j] == 0 for j in range(5)):
            bingo_cnt += 1
    
    # 세로줄 체크 - 수정된 로직  
    for j in range(5):
        if all(bingo[i][j] == 0 for i in range(5)):
            bingo_cnt += 1

    return bingo_cnt

def check_cross():
    bingo_cnt = 0
    
    # 주대각선 (왼쪽 위 -> 오른쪽 아래)
    if all(bingo[i][i] == 0 for i in range(5)):
        bingo_cnt += 1
    
    # 반대각선 (오른쪽 위 -> 왼쪽 아래)
    if all(bingo[i][4-i] == 0 for i in range(5)):
        bingo_cnt += 1

    return bingo_cnt

for i in range(len(num)):
    y, x = find_num(num[i])
    if y >= 0 and x >= 0:  # 수정된 조건
        bingo[y][x] = 0
    
    # 빙고 체크
    if i >= 4:  # 최소 5개는 지워져야 함
        total_bingo = check_rc() + check_cross()
        if total_bingo >= 3:
            print(i + 1)
            break