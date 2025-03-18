import sys

for _ in range(int(sys.stdin.readline())) :
    str = sys.stdin.readline().rstrip()
    print(str[0], str[-1], sep="")