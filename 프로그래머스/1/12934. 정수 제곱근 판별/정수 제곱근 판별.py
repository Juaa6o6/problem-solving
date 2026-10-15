def solution(n):
    x = n**0.5
    return (x+1)**2 if n // x == x else -1