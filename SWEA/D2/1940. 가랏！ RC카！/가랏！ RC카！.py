'''
command 가속값

command
= 1 -> +
= 2 -> -
= 0 -> 속도 유지

1 2 -> + 2
1 1 -> + 1
2 1 -> - 1
2 2 -> - 2
'''

T = int(input())

for tc in range(1, T+1):
    num = int(input())

    speed = 0
    now = 0
    for _ in range(num):
        lst = list(map(int, input().split()))

        if lst[0] == 1:
            now += lst[1]

        elif lst[0] == 2:
            now -= lst[1]
            if now < 0:
                now = 0

        speed += now

    print(f'#{tc} {speed}')
