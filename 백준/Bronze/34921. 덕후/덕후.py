n, m = map(int, input().split())
res = 10 + 2 * (25 - n + m)
if res < 0:
    print(0)
else:
    print(res)