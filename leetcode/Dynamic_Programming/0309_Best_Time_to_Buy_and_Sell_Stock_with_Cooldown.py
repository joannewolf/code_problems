class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        N = len(prices)
        if N <= 1:
            return 0

        INT_MIN = -100000
        # dp[i][0]: max profit until day i and not hold stock at the end
        # dp[i][1]: max profit until day i and hold stock at the end
        # dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        # dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        # while iterate i, only need to save dp[i - 2][0], dp[i - 1][0], dp[i - 1][1]
        # initial state for i = 2
        profit_0_pre = 0
        profit_0 = 0
        profit_1 = INT_MIN
        for i in range(N):
            profit_0_old = profit_0
            profit_0 = max(profit_0, profit_1 + prices[i]) # rest or sell
            profit_1 = max(profit_1, profit_0_pre - prices[i]) # rest or buy
            profit_0_pre = profit_0_old

        return profit_0
