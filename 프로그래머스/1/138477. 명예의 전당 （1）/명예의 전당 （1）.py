def solution(k, score):
    ans = []
    win = []
    for s in score:
        if len(win) == k:
            if win[-1] < s:
                win.pop()
                win.append(s)
        else:
            win.append(s)

        win.sort(reverse=True)
        ans.append(min(win))
    return ans