def solution(n, m, section):
    p = 0
    cnt = 0
    for s in section:
        if p < s:
            p = s + m - 1
            cnt += 1

    return cnt