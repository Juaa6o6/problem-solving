def recur(num, cnt):
    global d, n
    if cnt == d:
        return num

    total = num
    return recur(total*n, cnt+1)

for _ in range(10):
    T = int(input())
    n, d = map(int, input().split())
    res = recur(n, 1)

    print(f'#{T} {res}')