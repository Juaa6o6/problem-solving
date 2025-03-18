import sys

for _ in range(int(sys.stdin.readline())) :
    str = sys.stdin.readline().rstrip()
    sys.stdout.write(str[0] + str[-1] + '\n')