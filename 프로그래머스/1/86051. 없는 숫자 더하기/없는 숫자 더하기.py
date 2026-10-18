def solution(numbers):
    return sum(x if x not in numbers else 0 for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])