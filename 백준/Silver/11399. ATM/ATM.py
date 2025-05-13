count = int(input())
min_order = sorted(list(map(int, input().split())))
result = 0
i = count + 1
for order in min_order:
    i -= 1
    result += order * i
print(result)