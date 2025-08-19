T = int(input())

for tc in range(1, T+1):

    N = int(input())    # 나무 개수
    day = [1, 2] * (50*N)
    ori_tree = list(map(int, input().split()))  # 나무 높이
    max_height = max(ori_tree)  # 최대 높이

    for i in range(len(ori_tree)):
        ori_tree[i] = max_height - ori_tree[i]

    tree = [tree for tree in ori_tree if tree != 0]
    tree = sorted(tree)
    len_day = len(day)

    def day_check(idx):
        global tree, day

        for i in range(len_day):
            if day[i] != 0:
                if tree[idx] == 0:
                    break
                elif tree[idx] == 1:
                    if day[i] == 1:
                        tree[idx] -= day[i]
                        day[i] = 0
                elif tree[idx] == 2:
                    if day[i] == 2:
                        tree[idx] -= day[i]
                        day[i] = 0
                elif tree[idx] % 3 == 0:
                    tree[idx] -= day[i] + day[i + 1]
                    day[i], day[i + 1] = 0, 0
                else:
                    tree[idx] -= day[i]
                    day[i] = 0

    for i in range(len(tree)):
        day_check(i)

    growth_day = -1
    for i, value in enumerate(day):
        if value == 0:
            growth_day = i

    print(f'#{tc} {growth_day+1}')