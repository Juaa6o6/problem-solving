def solution(a, b):
    if a == b: return a
    res = 0
    s, f = min(a, b), max(a, b)
    for i in range(s, f+1):
        res += i
    return res