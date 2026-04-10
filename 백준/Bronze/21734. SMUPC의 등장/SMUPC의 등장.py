word = input()
wn = int(len(word))
num = 0
for w in range(wn):
    asc = str(ord(word[w]))
    for i in range(len(asc)):
        num += int(asc[i])
    print(word[w]*num)
    num = 0