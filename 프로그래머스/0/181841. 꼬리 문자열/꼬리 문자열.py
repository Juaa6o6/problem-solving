def solution(str_list, ex):
    ans = ""
    for sl in str_list:
        if not ex in sl:
            ans += sl
    return ans