def solution(t, p):
    ans = 0
    lp = len(p)
    for i in range(len(t)-lp+1):
        pt = t[i:i+lp]
        if pt <= p:
            ans += 1
            
    return ans