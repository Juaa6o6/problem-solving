def num_sum(w):
    num = 0
    for i in range(len(w)):
        num += int(asc[i])
    return num


word = input("")
wn = int(len(word))

for w in range(wn):
    asc = str(ord(word[w]))
    hap = num_sum(asc)
    print(word[w]*hap)