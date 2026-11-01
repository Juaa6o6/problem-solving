def solution(d, budget):
    d.sort()
    cnt = 0
    total = 0
    for i in d:
        total += i
        if total <= budget:
            cnt += 1
        else:
            return cnt
    
    return cnt