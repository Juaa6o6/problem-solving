def solution(sizes):
    w = []
    h = []
    for s in sizes:
        if s[0] < s[1]:
            s[0], s[1] = s[1], s[0]
        w.append(s[0])
        h.append(s[1])
    return max(w) * max(h) 