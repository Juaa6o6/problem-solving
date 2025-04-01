n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())
t_count = 0
for i in size:
    if i == 0:
        continue
    t_count += i//t
    t_each = i%t
    if t_each != 0:
        t_count += 1
print(t_count)
print((n//p), (n%p))
