import sys

N, M = map(int, sys.stdin.readline().split())

A = []

for a in range(N) :
    A.append(list(map(int, sys.stdin.readline().split())))

B = []
for b in range(N) :
    B.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    d = []
    a = A[i]
    b = B[i]
    for ii in range(M) :
        c = a[ii] + b[ii]
        d.append(c)
    print(" ".join(map(str, d)))