def solution(sizes):
    """ r, c = 0, 0
    for w, h in sizes:
        if w < h:
            w, h = h, w
        r = max(w, r)
        c = max(h, c)
    return r * c """
    return max(max(w) for w in sizes) * max(min(h) for h in sizes)
    