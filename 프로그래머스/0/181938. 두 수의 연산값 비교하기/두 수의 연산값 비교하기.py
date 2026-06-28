def solution(a, b):
    p = str(a) + str(b)
    n = 2 * a * b
    return int(p) if int(p) >= n else n