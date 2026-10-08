def solution(n):
    n -= 1
    s = int(n ** 0.5)
    
    for i in range(2, s+1):
        if n % i == 0:
            return i
        
    return n