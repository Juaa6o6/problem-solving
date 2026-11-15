def solution(name, yearning, photo):
    score = dict(zip(name, yearning))
    ans = []
    for pt in photo:
        hap = 0
        for p in pt:
            if p in score:
                hap += score[p]
        ans.append(hap)
    return ans