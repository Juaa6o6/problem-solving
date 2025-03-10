import sys

t = int(input())

for i in range(t) :
    a, b = map(int, sys.stdin.readline().split())
    i = a + b
    print(i)