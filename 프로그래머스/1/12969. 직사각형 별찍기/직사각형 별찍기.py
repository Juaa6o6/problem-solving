a, b = map(int, input().strip().split(' '))
for _ in range(b):
    for j in range(a):
        print('*', end='')
    print()