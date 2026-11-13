def solution(k, score):
    ans = []
    win = []
    for s in score:
        # 1. win에 k값 만큼 들어있는지 확인한다
        if len(win) == k:
            # 3. win의 최소값과 현재 점수를 비교 -> 현재 점수가 더 크면
            if win[-1] < s:
            # 4.  명예에 전당에 넣고 최소값은 뺀다.
                win.pop()
                win.append(s)
        # 2. k값 만큼 들어있지 않으면 추가한다.
        else:
            win.append(s)
            
        # 5. win 정렬한다.
        win.sort(reverse=True)
        # 6. win 최소값을 ans 에 넣는다
        ans.append(min(win))
    return ans