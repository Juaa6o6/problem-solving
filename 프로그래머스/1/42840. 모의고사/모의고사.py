def solution(ans):
    m1 = [1, 2, 3, 4, 5] * len(ans)
    m2 = [2, 1, 2, 3, 2, 4, 2, 5] * len(ans)
    m3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * len(ans)
    scores = [0] * 4
    
    for i in range(len(ans)):
        if ans[i] == m1[i]:
            scores[1] += 1
        if ans[i] == m2[i]:
            scores[2] += 1        
        if ans[i] == m3[i]:
            scores[3] += 1
            
    return [i for i, v in enumerate(scores) if max(scores) == v]