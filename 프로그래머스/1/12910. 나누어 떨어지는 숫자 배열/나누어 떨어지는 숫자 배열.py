def solution(arr, divisor):
    lst = sorted([x for x in arr if x % divisor == 0])
    return lst if lst else [-1]