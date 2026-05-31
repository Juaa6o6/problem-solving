def solution(n):
    answer = []
    for q in range(1, int(n**0.5) + 1):
        if n % q == 0:
            answer.append(q)
            if q != n // q:
                answer.append(n // q)
                
    answer.sort()
    return answer