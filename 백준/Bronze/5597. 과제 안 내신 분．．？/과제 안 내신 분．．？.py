import sys

n = list(map(int, sys.stdin.read().rstrip().split()))

for i in range(1, 31) :
    n.sort(reverse=True)
    if n.count(i) == False :
        print(i)