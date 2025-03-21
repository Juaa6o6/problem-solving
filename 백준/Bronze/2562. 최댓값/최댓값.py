import sys
n = list(map(int, sys.stdin.read().split()))
s = sorted(n)
print(s[-1])
print(n.index(s[-1])+1)