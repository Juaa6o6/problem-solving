import sys
input = sys.stdin.readline

T = int(input())
switch = list(map(int, input().split()))

ST = int(input())
for i in range(ST):
    S, N = map(int, input().split())

    if S == 1:
        for num in range(1, T+1):
            if num % N == 0:
                if switch[num-1] == 0:
                    switch[num-1] = 1
                else:
                    switch[num-1] = 0

    elif S == 2:
        N -= 1
        idx = 0
        for j in range(1, T//2):
            if N-j<0 or N+j<0 or N-j>T-1 or N+j>T-1: continue
            elif switch[N-j] == switch[N+j]:
                idx = j
            else:
                break
        for s in range(N-idx, N+idx+1):
            if switch[s]:
                switch[s] = 0
            else:
                switch[s] = 1

for i in range(0, len(switch), 20):
    print(*switch[i:i+20])