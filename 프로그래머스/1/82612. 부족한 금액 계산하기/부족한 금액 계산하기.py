def solution(price, money, count):
    ans = 0
    for c in range(1, count+1):
        ans += price * c
        
    return 0 if ans <= money else (ans - money)