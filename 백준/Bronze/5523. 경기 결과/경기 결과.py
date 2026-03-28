n = int(input())
a_win, b_win = 0, 0
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        a_win += 1
    elif b > a:
        b_win += 1

print(a_win, b_win)