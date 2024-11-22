class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        N, M = len(matrix), len(matrix[0])
        dp = [[0] * M for _ in range(N)] # dp[i][j]: the max square len which lower-right grid at matric[i][j]
        ones_row = 0 # the max len of horizontal consecutive 1's until current grid
        ones_column = [0] * M # the max len of vertical consecutive 1's until current row
        max_square_len = 0

        # initialize left-most column and upper-most row
        for i in range(N):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                max_square_len = 1
        for j in range(M):
            if matrix[0][j] == '1':
                dp[0][j] = 1
                ones_column[j] = 1
                max_square_len = 1

        for i in range(1, N):
            ones_row = dp[i][0]
            for j in range(1, M):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], ones_row, ones_column[j]) + 1
                    max_square_len = max(max_square_len, dp[i][j])
                    ones_row += 1
                    ones_column[j] += 1
                else:
                    ones_row = 0
                    ones_column[j] = 0

        return max_square_len * max_square_len