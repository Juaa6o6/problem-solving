def solution(food):
    ans = ''
    for i, f in enumerate(food[1:]):
        ans += (f // 2) * str(i+1)
    return ans + '0' + ans[::-1]