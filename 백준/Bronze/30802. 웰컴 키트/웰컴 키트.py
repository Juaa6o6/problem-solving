import sys
read = sys.stdin.readline
N = int(input())
size = list(map(int, read().split()))
T, P = map(int, read().split())
t_count = []
for i in size:
    t = i//T
    t_each = i%T
    if 0 < t_each < T:
        t += 1
    t_count.append(t)
print(sum(t_count))
print((N//P), (N%P))