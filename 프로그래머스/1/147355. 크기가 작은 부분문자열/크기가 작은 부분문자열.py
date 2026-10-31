def solution(t, p):
    ans = 0
    lp, p = len(p), int(p)

    for i in range(len(t)-lp+1):
        pt = t[i:i+lp]
        if int(pt) <= p:
            ans += 1
            
    return ans