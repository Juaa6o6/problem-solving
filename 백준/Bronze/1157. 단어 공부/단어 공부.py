st = input().upper()
lst = [0] * 91

for w in st:
    num = ord(w)
    lst[num] += 1

max_lst = []
max_rst = max(lst)

for idx, v in enumerate(lst):
    if v != 0:
        if max_rst <= v:
            max_rst = v
            max_lst.append(idx)

if len(max_lst) > 1:
    print('?')
else:
    print(chr(max_lst[0]))