def solution(name, yearning, photo):
    ans = []
    for p in photo:
        re = []
        for i in range(len(name)):
            if name[i] in p:
                re.append(yearning[i])
        ans.append(sum(re))
    return ans