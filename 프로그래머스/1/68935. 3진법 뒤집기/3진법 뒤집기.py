def solution(n):
    th = ''
    while n:
        th += str(n % 3)
        n = n // 3

    return int(th, 3)