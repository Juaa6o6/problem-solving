def solution(arr, divisor):
    return sorted([x for x in arr if x % divisor == 0]) if sorted([x for x in arr if x % divisor == 0]) else [-1]