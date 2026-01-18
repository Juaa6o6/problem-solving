t = int(input())
cnt = 0
for tc in range(t):
    word = input()
    now = ''
    lst = []
    dup = False

    for w in word:
        if w not in lst:
            if now != w:
                now = w
                lst.append(w)
        else:
            if now != w:
                dup = True
                break

    if not dup:
        cnt += 1

print(cnt)