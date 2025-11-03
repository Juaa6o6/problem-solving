T = int(input())

for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    n = lst[0]
    avg = sum(lst[1:])/n
    
    cnt = 0
    for i in range(1, n+1):
        if avg < lst[i]:
            cnt += 1
    
    print(f'{cnt/n*100:.3f}%')
