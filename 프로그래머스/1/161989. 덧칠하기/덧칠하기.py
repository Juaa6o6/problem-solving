def solution(n, m, s):
    ch = 0
    cnt = 0
    for i in range(len(s)):
        if ch < s[i]:
            ch = s[i] + m - 1
            cnt += 1

    return cnt