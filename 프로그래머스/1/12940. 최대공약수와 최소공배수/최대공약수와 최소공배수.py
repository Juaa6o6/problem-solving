def solution(n, m):
    mi, ma = 1000000, 0
    i = 0
    for _ in range(n*m):
        i += 1
        if n % i == 0 and m % i == 0:
            ma = i
        if i % n == 0 and i % m == 0:
            if mi > i:
                mi = i
    return ma, mi