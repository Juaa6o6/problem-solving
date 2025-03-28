import sys
while True:
    sides = list(map(int, sys.stdin.readline().strip().split()))
    if sides == [0, 0, 0]: 
        break
    sides.sort()
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        sys.stdout.write("right\n")
    else:
        sys.stdout.write("wrong\n")