# Matrix Cutting
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201b7d/0000000000201d2b
# DP, O(N^2*M^2(N+M))

INF = pow(10, 10)

def solve(i1, i2, j1, j2):
    if dp[i1][i2][j1][j2] != -1:
        return dp[i1][i2][j1][j2]

    if i1 == i2 and j1 == j2:
        dp[i1][i2][j1][j2] = 0
        return 0

    # Find the min value of current submatrice
    min_value = INF
    for i in range(i1, i2+1):
        for j in range(j1, j2+1):
            min_value = min(min_value, grid[i][j])

    submatrices = 0
    # Cut horizontally
    for gap_i in range(i2 - i1):
        submatrices = max(submatrices, solve(i1, i1 + gap_i, j1, j2) + solve(i1 + gap_i + 1, i2, j1, j2))
    # Cut vertically
    for gap_j in range(j2 - j1):
        submatrices = max(submatrices, solve(i1, i2, j1, j1 + gap_j) + solve(i1, i2, j1 + gap_j + 1, j2))

    dp[i1][i2][j1][j2] = min_value + submatrices
    return dp[i1][i2][j1][j2]

T = int(input())
for t in range(T):
    [N, M] = [int(x) for x in input().split()]
    grid = []
    for _ in range(N):
        grid.append([int(x) for x in input().split()])
    # for i in range(N):
    #     print(grid[i])

    dp = [[[[-1] * M for _ in range(M)] for _ in range(N)] for _ in range(N)]
    # dp[i1][i2][j1][j2]: the result of cutting submatrices grid[i1~i2][j1~j2], inclusive
    # 0 <= i1, i2 < N; 0 <= j1, j2 < M

    print(f"Case #{t + 1}: {solve(0, N-1, 0, M-1)}")
