def solution(number, limit, power):
    re = []
    for num in range(1, number + 1):
        div = []
        total = 0
        for n in range(1, int(num ** 0.5) + 1):
            if num % n == 0:
                q = num // n
                if n != q:
                    div.extend([n, q])
                else:
                    div.append(n)

        if len(div) > limit:
            total = power
        else:
            total = len(div)
        re += [total]
    return sum(re)