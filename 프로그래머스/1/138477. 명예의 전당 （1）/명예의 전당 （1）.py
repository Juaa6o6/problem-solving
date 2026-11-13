def solution(k, score):
    ans = []
    q = []
    for s in score:
        q.append(s)
        if len(q) > k:
            q.remove(min(q))

        ans.append(min(q))
    return ans