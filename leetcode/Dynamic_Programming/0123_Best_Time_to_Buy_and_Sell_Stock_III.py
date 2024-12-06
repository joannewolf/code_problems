class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        INT_MIN = -1000000
        N = len(prices)
        # dp[i][k][0]: max profit until day i with at most k transactions and not hold stock at the end
        # dp[i][k][1]: max profit until day i with at most k transactions and hold stock at the end
        # dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]), rest or sell at day i
        # dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]), rest or buy at day i
        # while iterate i, only need to save previous day number
        profit_k2_0 = 0
        profit_k2_1 = INT_MIN
        profit_k1_0 = 0
        profit_k1_1 = INT_MIN
        for i in range(N):
            profit_k2_0 = max(profit_k2_0, profit_k2_1 + prices[i])
            profit_k2_1 = max(profit_k2_1, profit_k1_0 - prices[i])
            profit_k1_0 = max(profit_k1_0, profit_k1_1 + prices[i])
            profit_k1_1 = max(profit_k1_1, - prices[i]) # profit_k0_0 always = 0

        return profit_k2_0
