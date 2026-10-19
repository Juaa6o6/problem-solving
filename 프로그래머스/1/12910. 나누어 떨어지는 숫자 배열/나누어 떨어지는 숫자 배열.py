def solution(arr, divisor):
    cnt = 0
    lst = []
    for a in arr:
        if a % divisor == 0:
            lst.append(a)
            cnt += 1
    
    if cnt != 0:
        return sorted(lst)
    else:
        return [-1]