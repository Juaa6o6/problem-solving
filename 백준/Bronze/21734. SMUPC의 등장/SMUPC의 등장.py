word = input()
wn = int(len(word))
for w in range(wn):
    num = 0
    asc = str(ord(word[w]))
    for i in range(len(asc)):
        num += int(asc[i])
    print(f'{word[w]*num}')