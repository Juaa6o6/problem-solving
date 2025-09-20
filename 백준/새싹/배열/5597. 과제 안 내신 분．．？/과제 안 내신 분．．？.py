import sys

n = list(map(int, sys.stdin.read().split()))

for i in range(1, 31) :
    n.sort()
    if n.count(i) == False :
        print(i)