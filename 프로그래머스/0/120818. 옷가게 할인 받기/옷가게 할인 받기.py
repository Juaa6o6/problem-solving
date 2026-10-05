def solution(price):
    dis = 0
    if price >= 500000:
        dis = price * 0.2
    elif price >= 300000:
        dis = price * 0.1
    elif price >= 100000:
        dis = price * 0.05
    return int(price - dis)