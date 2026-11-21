def solution(number, limit, power):
    result = [0] * (number + 1)
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            result[j] += 1
            
    return sum(power if re > limit else re for re in result[1:])