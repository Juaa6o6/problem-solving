T = int(input())

for tc in range(1, T+1):
    num = int(input())

    speed = 0
    now = 0
    for _ in range(num):
        lst = list(map(int, input().split()))

        if lst == [1, 2]:
            now += 2
        elif lst == [1, 1]:
            now += 1
        elif lst == [2, 1]:
            now -= 1
            if now < 0:
                now = 0
        elif lst == [2, 2]:
            now -= 2
            if now < 0:
                now = 0
        elif lst == [0]:
            now = now

        speed += now

    print(f'#{tc} {speed}')
