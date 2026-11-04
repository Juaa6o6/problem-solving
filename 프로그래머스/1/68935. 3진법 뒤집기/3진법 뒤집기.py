def solution(n):
    th = []
    while n:
        th.append(n % 3)
        n = n // 3
    reth = th[::-1]
    ans = 0
    for i in range(len(reth)-1,-1,-1): 
        ans += reth[i] * (3 ** i)
    return ans