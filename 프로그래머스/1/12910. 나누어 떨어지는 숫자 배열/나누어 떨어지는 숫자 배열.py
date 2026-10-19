def solution(arr, divisor):
    lst = [x for x in arr if x % divisor == 0]
    return sorted(lst) if lst else [-1]