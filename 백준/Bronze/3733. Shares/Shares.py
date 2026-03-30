import sys

for line in sys.stdin:
    n, s = map(int, line.strip().split())
    n += 1
    print(s//n)