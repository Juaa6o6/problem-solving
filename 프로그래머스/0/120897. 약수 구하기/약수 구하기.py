def solution(n):
    a = [q for q in range(1, int(n**0.5)+1) if n % q == 0]
    return a + [n // Q for Q in reversed(a) if Q != n // Q]