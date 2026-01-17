word = list(input())
cnt = len(word)

cro = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

for i in range(cnt):
    if word[i] in ['=', '-', 'j']:
        if word[i-2] + word[i-1] + word[i] == 'dz=':
            cnt -= 2
        elif word[i-1] + word[i] in cro:
            cnt -= 1

print(cnt)