word = input()
dial_groups = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
total_time = 0

for w in word:
    for i, group in enumerate(dial_groups):
        if w in group:
            total_time += i + 3
            break

print(total_time)