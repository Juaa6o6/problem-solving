def solution(n, m, s):
    ch = [False] * (n + 1)
    cnt = 0
    for i in range(len(s)):
        st = s[i]
        ed = st + m
        if ch[st] == False:
            if ed > n: ed = n + 1
            for c in range(st, ed):
                ch[c] = True
            cnt += 1

    return cnt