def solution(arr, divisor):
    lst = ([x for x in arr if x % divisor == 0])
    if lst :
        return sorted(lst)
    else:
        return [-1]