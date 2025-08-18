L = int(input())

roll = [0]*(L+1)

N = int(input())
peo = []

for i in range(N):
    pk = list(map(int, input().split()))
    peo.append(pk)

expect_max = 0
expect_max_idx = -1
for i in range(len(peo)):
    a, b = peo[i]
    if expect_max < b - a + 1:
        expect_max = b - a + 1
        expect_max_idx = i+1

    for j in range(a, b+1):
        if roll[j] == 0:
            roll[j] = i+1

roll.pop(0)

real_max = 0
real_max_idx = -1
real_cnt = 0
for i in range(len(peo)):
    real_cnt = roll.count(i+1)
    if real_max < real_cnt:
        real_max = real_cnt
        real_max_idx = i+1

print(expect_max_idx, real_max_idx, sep='\n')