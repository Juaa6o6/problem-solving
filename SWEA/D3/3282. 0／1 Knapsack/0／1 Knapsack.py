T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())

    stuff = [(0, 0)]
    for _ in range(N):
        v, c = map(int, input().split())
        stuff.append((v, c))

    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        current_vol = stuff[i][0]
        current_val = stuff[i][1]

        for j in range(1, K + 1):
            if current_vol > j:
                dp[i][j] = dp[i - 1][j]

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - current_vol] + current_val)

    print(f'#{t} {dp[N][K]}')