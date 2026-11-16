def solution(cards1, cards2, goal):
    i, j = 0, 0
    for go in goal:
        if i < len(cards1) and go == cards1[i]:
            i += 1
        elif j < len(cards2) and go == cards2[j]:
            j += 1
        else:
            return "No"
    return "Yes"