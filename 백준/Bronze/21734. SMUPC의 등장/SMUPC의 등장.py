word = input()
for w in word:
    num = 0
    asc = str(ord(w))
    for i in range(len(asc)):
        num += int(asc[i])
    print(f'{w*num}')