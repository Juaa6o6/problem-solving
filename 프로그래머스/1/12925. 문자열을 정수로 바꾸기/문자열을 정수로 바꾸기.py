def solution(s):
    if s[0] == '-':
        return 0 - int(s[1:])
    else:
        return int(s)