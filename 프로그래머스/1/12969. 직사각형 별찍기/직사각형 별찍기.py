a, b = map(int, input().strip().split(' '))
ans = ('*' * a + '\n') * b
print(ans)

"""
for _ in range(b):
    for j in range(a):
        print('*', end='')
    print()
"""