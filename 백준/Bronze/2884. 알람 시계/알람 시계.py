h, m = map(int, input().split())

c = (60*h + m)-45

if c < 0:
    c += 1440

print(c//60, c%60)