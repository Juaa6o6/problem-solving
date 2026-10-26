def solution(l, r):
    ans = 0
    for i in range(l, r+1):
        if int(i**0.5) == i**0.5:
            ans -= i
        else:
            ans += i
            
    return ans