N = int(input())    # 기둥 수

ware = [0]*1001

for _ in range(N):
    L, H = map(int, input().split())
    ware[L] = H

H_max = max(ware)

start_idx=0
end_idx=0
for i in range(1, 1001):
    if ware[i] != 0:
        start_idx = i
        break

for i in range(1000, 0, -1):
    if ware[i] != 0:
        end_idx = i
        break

ware_house = ware[start_idx:end_idx+1]
# max_idx = [i for i, x in enumerate(ware_house) if x == H_max]
w_ware = len(ware_house)
max_idx = ware_house.index(H_max)

pre_max = 0
for i in range(max_idx):
    if ware_house[i] != 0:
        if pre_max <= ware_house[i]:
            pre_max = ware_house[i]
        else:
            ware_house[i] = pre_max
    else:
        ware_house[i] = pre_max

post_max = 0
for i in range(w_ware-1, max_idx, -1):
    if ware_house[i] != 0:
        if post_max <= ware_house[i]:
            post_max = ware_house[i]
        else:
            ware_house[i] = post_max
    else:
        ware_house[i] = post_max

box = [[0]*H_max for _ in range(w_ware)]
area = 0
for i in range(w_ware):
    for j in range(ware_house[i]):
        box[i][j] = 1
        area += 1

print(area)