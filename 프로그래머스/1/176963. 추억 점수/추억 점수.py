def solution(name, yearning, photo):
    return [sum(yearning[name.index(i)] for i in p if i in name) for p in photo]