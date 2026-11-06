def solution(s):
    ans = []
    last = {}
    for i, c in enumerate(s):
        if c in last:
            ans.append(i-last[c])
        else:
            ans.append(-1)
            
        last[c] = i

    return ans