def solution(number, limit, power):
    result = 0
    for num in range(1, number + 1):
        cnt = 0
        for n in range(1, int(num ** 0.5) + 1):
            if num % n == 0:
                q = num // n
                if n != q:
                    cnt += 2
                else:
                    cnt += 1

        if cnt > limit:
            result += power
        else:
            result += cnt
            
    return result