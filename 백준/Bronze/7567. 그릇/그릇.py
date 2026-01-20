bowls = input()
now = ''
total = 0

for bowl in bowls:
    if now != bowl:
        now = bowl
        total += 10

    else:
        total += 5


print(total)