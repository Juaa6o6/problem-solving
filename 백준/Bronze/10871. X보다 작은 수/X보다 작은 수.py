import sys

N, X = map(int, sys.stdin.readline().split())
for a in map(int, sys.stdin.readline().split()):
    if a < X:
        sys.stdout.write(f'{a} ')