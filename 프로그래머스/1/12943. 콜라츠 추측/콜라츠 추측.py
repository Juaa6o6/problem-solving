def solution(num):
    for cnt in range(500):

        if num == 1:
            return cnt
        
        num = num // 2 if num % 2 == 0 else num * 3 + 1
        
    return 500 if num == 1 else -1