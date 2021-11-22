# Plates
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d40bb

T = int(input())
for t in range(T):
    [N, K, P] = [int(n) for n in input().split()]
    plates = []
    for i in range(N):
        plates.append([0] + [int(n) for n in input().split()])

    # Sum up plates
    for i in range(N):
        for j in range(1, K+1):
            plates[i][j] += plates[i][j - 1]
        # print(plates[i])

    dp = [[0] * (P+1) for i in range(N+1)]
    # dp[i][j]: with i stack of plates, the max beauty value for j plates
    for i in range(1, N+1):
        for j in range(min(i * K, P) + 1):
            max_value = 0
            for k in range(min(j, K) + 1): # Take k plate in current i-th stack
                max_value = max(max_value, dp[i - 1][j - k] + plates[i - 1][k])
            dp[i][j] = max_value
    # for i in range(N+1):
    #     print(dp[i])

    print(f"Case #{t + 1}: {dp[N][P]}")
