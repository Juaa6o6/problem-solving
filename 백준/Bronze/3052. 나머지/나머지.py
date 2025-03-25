import sys
num = sys.stdin.read().strip().split()
d = set()
for n in num:
    d.add(int(n)%42)
print(len(d))