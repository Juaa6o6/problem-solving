def solution(s):
    lth = len(s)
    return s[lth//2-1 : lth//2+1] if lth % 2 == 0 else s[lth//2]