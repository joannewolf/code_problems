# Sightseeing
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201b77/0000000000201bfd
# DP, O(N^2)

import math

INF = pow(10, 10)

T = int(input())
for t in range(T):
    [N, T_S, T_F] = [int(x) for x in input().split()]
    bus = []
    for _ in range(N-1):
        [s, f, d] = [int(x) for x in input().split()]
        bus.append((s, f, d))

    dp = [[INF] * N for _ in range(N)]
    # dp[i][j]: the min time to reach city i while sightseeing j cities
    dp[0][0] = 0
    for i in range(1, N):
        (S, F, D) = bus[i - 1]

        x = max(math.ceil((dp[i - 1][0] - S) / F), 0)
        dp[i][0] = S + x * F + D

        for j in range(1, i):
            x = max(math.ceil((dp[i - 1][j] - S) / F), 0)
            option1 = S + x * F + D
            x = max(math.ceil((dp[i - 1][j - 1] + T_S - S) / F), 0)
            option2 = S + x * F + D
            dp[i][j] = min(option1, option2)

        x = max(math.ceil((dp[i - 1][i - 1] + T_S - S) / F), 0)
        dp[i][i] = S + x * F + D

    # for i in range(N):
    #     print(dp[i][0: i+1])

    ans = -1
    for j in range(N):
        if dp[N-1][j] <= T_F:
            ans = j
    if ans == -1:
        print(f"Case #{t + 1}: IMPOSSIBLE")
    else:
        print(f"Case #{t + 1}: {ans}")
