for _ in range(int(input())):
    ox = input()
    box = 'O'*len(ox)
    s_box = []
    score = 0
    for i in range(len(ox)):
        if ox[i] == box[i]:
            score += 1
            s_box.append(score)
        else:
            score = 0
            s_box.append(score)
    print(sum(s_box))