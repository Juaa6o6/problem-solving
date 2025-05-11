import sys

input = sys.stdin.readline
n, m = map(int, input().split())

heard = set(input().strip() for _ in range(n))

result = []
for _ in range(m):
    name = input().strip()
    if name in heard:
        result.append(name)

result.sort()
print(len(result))
print('\n'.join(result))