dial = input()
total = 0
for w in dial:
    if w in ['A', 'B', 'C']:
        total += 3
    elif w in ['D', 'E', 'F']:
        total += 4
    elif w in ['G', 'H', 'I']:
        total += 5
    elif w in ['J', 'K', 'L']:
        total += 6
    elif w in ['M', 'N', 'O']:
        total += 7
    elif w in ['P', 'Q', 'R', 'S']:
        total += 8
    elif w in ['T', 'U', 'V']:
        total += 9
    elif w in ['W', 'X', 'Y', 'Z']:
        total += 10

print(total)