def solution(num):
    n = 0
    if num[-1] > num[-2]:
        n = num[-1] - num[-2]
    else:
        n = num[-1] * 2
    num.append(n)
    return num