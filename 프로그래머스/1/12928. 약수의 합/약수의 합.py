def solution(n):
    hap = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            q = n // i
            if i != q:
                hap += i + q
            else:
                hap += i
            
    return hap