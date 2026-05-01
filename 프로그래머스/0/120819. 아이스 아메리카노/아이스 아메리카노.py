def solution(money):
    answer = []
    americano = 5500
    pos = money // americano
    cha = money % americano
    answer.append(pos)
    answer.append(cha)
    return answer