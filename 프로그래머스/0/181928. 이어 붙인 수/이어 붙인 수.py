def solution(num_list):
    odd, eve = '', ''
    for n in num_list:
        if n % 2 == 0:
            eve += str(n)
        else:
            odd += str(n)
    return int(odd) + int(eve)