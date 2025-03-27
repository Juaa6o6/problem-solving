import sys
for i in range(int(input())):
    H, W, N = map(int, sys.stdin.readline().split())
    room = []
    for w in range(1, W+1):
        if w < 10:
                w = '0'+ str(w)
        else:
             w = str(w)
        for h in range(1, H+1):
            room_num = str(h)+w
            room.append(room_num)
    print(room[N-1])