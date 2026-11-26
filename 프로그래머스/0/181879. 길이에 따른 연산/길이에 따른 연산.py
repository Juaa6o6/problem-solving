def solution(num_list):
    ans = 1
    if len(num_list) >= 11:
        ans = sum(num_list)
    elif len(num_list) <= 10:
        for num in num_list:
            ans *= num
    return ans