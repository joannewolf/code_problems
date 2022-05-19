# Catch Them All
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201d29/0000000000201c9b
# DP, O(N^3 + N^2*P), TLE on test set 2

INF = pow(10, 5)

T = int(input())
for t in range(T):
    [N, M, P] = [int(x) for x in input().split()]
    dist = [[INF] * N for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0
    for _ in range(M):
        [u, v, d] = [int(x) for x in input().split()]
        dist[u-1][v-1] = d
        dist[v-1][u-1] = d

    # Use Floyd–Warshall algorithm to find all pairs of shortest paths
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    # for i in range(N):
    #     print(dist[i])

    # Origin DP, MLE on test set 2
    # dp = [[0] * N for _ in range(P+1)]
    # dp[i][v]: The expected time to catch i Codejamons when starting from location v
    # for i in range(1, P+1):
    #     for v in range(N):
    #         for u in range(N):
    #             if u != v:
    #                 dp[i][v] += dp[i - 1][u] + dist[u][v]
    #         dp[i][v] /= (N - 1)
    # print(f"Case #{t + 1}: {dp[P][0]}")

    # Memory-optimized DP
    # Since it only needs dp[i - 1] to calculate dp[i], we only maintain the dp[v] for current i
    dp = [0] * N
    for i in range(1, P+1):
        next_dp = [0] * N
        for v in range(N):
            for u in range(N):
                if u != v:
                    next_dp[v] += dp[u] + dist[u][v]
            next_dp[v] /= (N - 1)
        dp = next_dp

    print(f"Case #{t + 1}: {dp[0]}")
