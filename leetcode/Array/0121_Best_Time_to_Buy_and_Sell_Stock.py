class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        N = len(prices)
        slow, fast = 0, 1
        max_profit = 0
        while fast < N:
            if prices[fast] > prices[slow]:
                max_profit = max(max_profit, prices[fast] - prices[slow])
                fast += 1
            else:
                slow = fast
                fast += 1

        return max_profit
