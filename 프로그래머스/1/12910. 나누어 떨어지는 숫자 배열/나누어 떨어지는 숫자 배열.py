def solution(arr, divisor):
    lst = ([x for x in arr if x % divisor == 0])
    if len(lst) != 0:
        return sorted(lst)
    else:
        return [-1]