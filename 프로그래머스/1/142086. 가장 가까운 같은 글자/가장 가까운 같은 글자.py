def solution(s):
    ans = []
    ch = {}
    p = {}
    for i in range(len(s)):
        if s[i] not in ch:
            ch[s[i]] = i
            ans.append(-1)
        else:
            if s[i] not in p:
                p[s[i]] = i
                ans.append(p[s[i]]-ch[s[i]])
            else:
                ans.append(min(i-p[s[i]], i-ch[s[i]]))
                p[s[i]] = i
    return ans