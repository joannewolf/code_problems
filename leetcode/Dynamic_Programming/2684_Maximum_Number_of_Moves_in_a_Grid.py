class Solution(object):
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N, M = len(grid), len(grid[0])
        dp = [] # dp[i][j] means the max move starting from grid[i][j]
        for _ in range(N):
            dp.append([0] * M)

        # traverse column from right to left
        for j in range(M - 2, -1, -1):
            for i in range(N):
                if i == 0:
                    if grid[i][j] < grid[i][j+1]:
                        dp[i][j] = max(dp[i][j], dp[i][j+1] + 1)
                    if grid[i][j] < grid[i+1][j+1]:
                        dp[i][j] = max(dp[i][j], dp[i+1][j+1] + 1)
                elif i == N - 1:
                    if grid[i][j] < grid[i-1][j+1]:
                        dp[i][j] = max(dp[i][j], dp[i-1][j+1] + 1)
                    if grid[i][j] < grid[i][j+1]:
                        dp[i][j] = max(dp[i][j], dp[i][j+1] + 1)
                else:
                    if grid[i][j] < grid[i-1][j+1]:
                        dp[i][j] = max(dp[i][j], dp[i-1][j+1] + 1)
                    if grid[i][j] < grid[i][j+1]:
                        dp[i][j] = max(dp[i][j], dp[i][j+1] + 1)
                    if grid[i][j] < grid[i+1][j+1]:
                        dp[i][j] = max(dp[i][j], dp[i+1][j+1] + 1)

        result = 0
        for i in range(N):
            result = max(result, dp[i][0])
        return result
