def solution(food):
    ans = ''
    for i in range(1, len(food)):
        ans += (food[i] // 2) * str(i)
    return ans + '0' + ans[::-1]