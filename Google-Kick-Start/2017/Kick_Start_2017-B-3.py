# Christmas Tree
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201d27/0000000000201c9a
# DP, O(NMK*NM)

MIN_INT = -pow(10, 9)

T = int(input())
for t in range(T):
    [N, M, K] = [int(x) for x in input().split()]
    grid = []
    for _ in range(N):
        grid.append(input())

    prefix = [[0] for _ in range(N)]
    # prefix[i][j]: # of greens between grid[i][0] ~ grid[i][j], inclusive
    dp = [[[MIN_INT] * (K+1) for _ in range(M)] for _ in range(N+1)]
    # dp[i][j][k]: the max # of greens of k-tree starting at grid[i][j]
    for i in range(N+1):
        for j in range(M):
            dp[i][j][0] = 0

    for i in range(N):
        for j in range(M):
            prefix[i].append(prefix[i][-1] + int(grid[i][j] == '#'))
    # for i in range(N):
    #     print(prefix[i])
    
    for k in range(1, K+1):
        for i in range(N-1, -1, -1):
            for j in range(M):
                if grid[i][j] == '#':
                    for level in range(N - i):
                        row = i + level
                        l = j - level
                        r = j + level
                        if l < 0 or r >= M or prefix[row][r+1] - prefix[row][l] != r - l + 1:
                            break
                        tree = (level + 1) * (level + 1)
                        for x in range(l, r+1):
                            dp[i][j][k] = max(dp[i][j][k], tree + dp[row + 1][x][k - 1])
                        # print("i", i, "j", j, "k", k, "level", level, dp[i][j][k])

    ans = 0
    for i in range(N):
        for j in range(M):
            ans = max(ans, dp[i][j][K])

    print(f"Case #{t + 1}: {ans}")
