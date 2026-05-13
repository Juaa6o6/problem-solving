def solution(n):
    sol = {1, n}
    for i in range(2, n+1):
        if n % i == 0:
            sol.update([i, n // i])
            
    return len(sol)