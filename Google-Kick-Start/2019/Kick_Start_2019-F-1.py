# Flattening
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edc/000000000018666c
# Using DP, O(KN^2)

def add_map(map: map, key: int):
    if key not in map:
        map[key] = 1
    else:
        map[key] += 1

T = int(input())
for t in range(T):
    [N, K] = [int(x) for x in input().split()]
    walls = [int(x) for x in input().split()]

    change = [[-1] * N for _ in range(N)]
    # change[i][j]: # of walls required to change to make wall i ~ j have the same height
    # -> all walls should follow the height appeared the most
    for i in range(N):
        count = {}
        for j in range(i, N):
            add_map(count, walls[j])
            change[i][j] = (j - i + 1) - max(count.values())
        # print(change[i])

    dp = [[N] * (K + 1) for _ in range(N)]
    # dp[x][k]: within wall 0 ~ x, min # of walls to change to achieve wall height diff <= k places
    # dp[x][k] = min(dp[i][k-1] + change[i+1][x]) for i = 1 ~ x-1
    for i in range(N):
        dp[i][0] = change[0][i]
    for k in range(K+1):
        dp[0][k] = 0
    for k in range(1, K+1):
        for x in range(N):
            for i in range(x):
                if dp[i][k - 1] + change[i + 1][x] < dp[x][k]:
                    dp[x][k] = dp[i][k - 1] + change[i + 1][x]
    # print()
    # for i in range(N):
    #     print(dp[i])

    print(f"Case #{t + 1}: {dp[N-1][K]}")
