import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    paper = list(map(int, input().split()))
    Max = max(paper)
    paper = [(v, 0) for v in paper]
    paper[m] = (paper[m][0], 1)

    cnt = 0

    while n:
        num, t = paper.pop(0)
        if num == Max and t:
            cnt += 1
            print(cnt)
            break
        else:
            if num != Max:
                paper.append((num, t))
            else:
                cnt += 1
                n -= 1
                Max = max(paper)
                Max = Max[0]