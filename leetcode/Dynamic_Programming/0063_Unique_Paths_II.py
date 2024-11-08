class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        # dp[i][j]: the number of paths from grid[i][j] to grid[m-1][n-1]
        dp = [[0] * N for _ in range(M)]
        for i in range(M - 1, -1, -1):
            if obstacleGrid[i][N - 1] == 0:
                dp[i][N - 1] = 1
            else:
                break
        for j in range(N - 1, -1, -1):
            if obstacleGrid[M - 1][j] == 0:
                dp[M - 1][j] = 1
            else:
                break

        for i in range(M - 2, -1, -1):
            for j in range(N - 2, -1, -1):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]