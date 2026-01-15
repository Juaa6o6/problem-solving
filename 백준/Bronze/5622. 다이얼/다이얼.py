word = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0

for w in word:
    for i, group in enumerate(dial):
        if w in group:
            time += i + 3
            break

print(time)