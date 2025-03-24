alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
w = input()
for a in alpha:
    if a in w:
        alpha[alpha.index(a)] = w.index(a)
    else:
        alpha[alpha.index(a)] = -1
print(*alpha)