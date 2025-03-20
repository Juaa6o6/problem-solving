import sys
a, b, c = map(int, sys.stdin.read().split())
n = str(a*b*c)
for i in range(10):
    print(n.count(str(i)))