word = input()
for w in word:
    asc = list(str(ord(w)))
    num = sum(map(int, asc))
    print(f'{w*num}')