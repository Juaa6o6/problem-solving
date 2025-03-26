for _ in range(int(input())):
    t, w = input().split()
    all = []
    for i in w:
        word = i*int(t)
        all.append(word)
    print("".join(all))