import sys
readline = sys.stdin.readline
S = set()
for i in range(int(input())):
    O = list(readline().split())
    order = O[0]
    if order == 'all':
        for e in range(1, 21):
            S.update([e])
    elif order == 'empty':
        S.clear()
    else:
        n = int(O[1])

    if order == 'check':
        if n in S:
            print(1)
        else:
            print(0)
    elif order == 'add':
        S.add(n)
        continue
    elif order == 'remove':
        S.discard(n)
        continue
    elif order == 'toggle':
        if n in S:
            S.discard(n)
        else:
            S.add(n)