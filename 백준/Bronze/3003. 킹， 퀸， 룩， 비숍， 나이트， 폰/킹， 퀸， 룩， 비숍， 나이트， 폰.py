correct = [1, 1, 2, 2, 2, 8]

found = list(map(int, input().split()))

for i in range(6):
    print(correct[i] - found[i], end=' ')