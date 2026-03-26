n, k = map(int, input().split())

now = 0 
now += k

for i in range(1, n+1):
    if i == n:
        print('비와이')        
    a, b = map(int, input().split())
    now += a
    now -= b