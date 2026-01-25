import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    paper = list(map(int, input().split()))

    q = [(idx, v) for idx, v in enumerate(paper)]

    sorted_paper = sorted(paper, reverse=True)

    cnt = 0

    while True:
        now_idx, now_v = q.pop(0)
        if now_v == sorted_paper[cnt]:
            if now_idx == m:
                print(cnt+1)
                break
            else:
                cnt += 1
        else:
            q.append((now_idx, now_v))