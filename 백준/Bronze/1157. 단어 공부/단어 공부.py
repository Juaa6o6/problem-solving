st = input().upper()
lst = [0] * 91

for w in st:
    num = ord(w)
    lst[num] += 1

if lst.count(max(lst)) >= 2:
    print("?")
else:
    print(chr(lst.index(max(lst))))