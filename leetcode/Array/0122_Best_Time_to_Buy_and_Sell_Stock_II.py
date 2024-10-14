class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        N = len(prices)
        profit = 0
        for i in range(N - 1):
            if prices[i + 1] - prices[i] > 0:
                profit += (prices[i + 1] - prices[i])

        return profit
