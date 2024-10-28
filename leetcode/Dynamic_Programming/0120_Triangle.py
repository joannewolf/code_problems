# O(N^2), O(N) space
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        N = len(triangle)
        # dp[i] means min val from triangle[row][i] to bottom
        # only need to save one row of value at a time
        dp = triangle[-1]
        for n in range(N - 1, 0, -1):
            new_dp = []
            for i in range(n):
                new_dp.append(triangle[n - 1][i] + min(dp[i], dp[i + 1]))
            dp = new_dp

        return dp[0]
