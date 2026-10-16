def solution(x, n):
    ans = []
    num = x
    for _ in range(n):
        ans.append(num)
        num += x
    return ans