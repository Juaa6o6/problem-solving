T = int(input())

for _ in range(1, T+1):
    line = list(map(int, input().split()))
    tc = line.pop(0)

    cnt = 0
    for i in range(1, len(line)):
        idx = i
        for j in range(i-1, -1, -1):
            if line[j] > line[idx]:
                line[idx], line[j] = line[j], line[idx]
                cnt += 1
                idx = j
            else:
                break

    print(f'{tc} {cnt}')