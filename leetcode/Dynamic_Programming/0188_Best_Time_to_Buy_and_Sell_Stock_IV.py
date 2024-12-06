class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        INT_MIN = -1000000
        N, K = len(prices), k + 1
        # dp[i][k][0]: max profit until day i with at most k transactions and not hold stock at the end
        # dp[i][k][1]: max profit until day i with at most k transactions and hold stock at the end
        # dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]), rest or sell at day i
        # dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]), rest or buy at day i
        # while iterate i, only need to save previous day number
        profit_0 = [0] * K
        profit_1 = [INT_MIN] * K
        for i in range(N):
            for j in range(k, 0, -1):
                profit_0[j] = max(profit_0[j], profit_1[j] + prices[i])
                profit_1[j] = max(profit_1[j], profit_0[j - 1] - prices[i])

        return profit_0[k]
