def solution(numbers):
    # 45 - sum(numbers)
    return sum(x if x not in numbers else 0 for x in range(10))