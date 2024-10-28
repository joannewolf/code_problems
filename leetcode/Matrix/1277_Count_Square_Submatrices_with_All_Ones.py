class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        N, M = len(matrix), len(matrix[0])
        result = 0
        dp = [] # dp[i][j] means the max square with matrix[i][j] as upper-left corner
        # initial with side 1 square
        for i in range(N):
            row = []
            for j in range(M):
                if matrix[i][j] == 1:
                    result += 1
                row.append(matrix[i][j])
            dp.append(row)

        for side_len in range(2, min(N, M) + 1):
            no_square = True
            for i in range(N - side_len + 1):
                for j in range(M - side_len + 1):
                    if (
                        dp[i][j] == side_len - 1 and
                        dp[i][j+1] == side_len - 1 and
                        dp[i+1][j] == side_len - 1 and
                        dp[i+1][j+1] == side_len - 1
                    ):
                        result += 1
                        dp[i][j] = side_len
                        no_square = False

            if no_square:
                break

        return result
