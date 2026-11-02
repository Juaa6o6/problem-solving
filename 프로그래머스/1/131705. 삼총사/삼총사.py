def solution(num):
    n = len(num)
    cnt = 0
    ch = [0] * n
    de = []
    for i in range(n):
        ch[i] = 1
        for j in range(n):
            if ch[j] == 1: continue
            ch[j] = 1
            for l in range(n):
                if ch[l] == 1: continue
                if num[i] + num[j] + num[l] == 0:
                    if {i, j, l} not in de:
                        de.append({i, j, l})
                        cnt += 1
                ch[l] = 0
            ch[j] = 0
        ch[i] = 0

    return cnt
                    
            
    