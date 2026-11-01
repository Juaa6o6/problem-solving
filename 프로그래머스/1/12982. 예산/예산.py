def solution(d, budget):
    d.sort()
    cnt = 0
    for cost in d:
        if budget < cost:
            break
        budget -= cost
        cnt += 1
    
    return cnt