def solution(n, k):
    meet = 12000
    cola = 2000
    c = k - (n // 10)
    answer = (n * meet) + (c * cola)
    return answer