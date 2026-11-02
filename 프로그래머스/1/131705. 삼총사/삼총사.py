def solution(num):
    n = len(num)
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            for l in range(j+1, n):
                if num[i] + num[j] + num[l] == 0:
                    cnt += 1

    return cnt
                    
            
    