def min_sugar_bags(N):
    for x in range(N // 5, -1, -1):
        R = N - (x * 5)
        if R % 3 == 0:
            return x + (R // 3)
    return -1
N = int(input())
print(min_sugar_bags(N))
