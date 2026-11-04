def solution(n):
    th = []
    while n:
        th.append(n % 3)
        n = n // 3
    ans = 0
    i = 0
    while th:
        ans += th.pop() * (3 ** i)
        i += 1
    return ans