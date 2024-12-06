# DP
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        INT_MIN = -100000
        N = len(prices)
        # dp[i][0]: max profit until day i and not hold stock at the end
        # dp[i][1]: max profit until day i and hold stock at the end
        # dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        # dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)
        # while iterate i, only need to save previous day number
        profit_0 = 0
        profit_1 = INT_MIN
        for i in range(N):
            old_profit_0 = profit_0
            profit_0 = max(profit_0, profit_1 + prices[i]) # rest or sell
            profit_1 = max(profit_1, old_profit_0 - prices[i] - fee) # rest or buy

        return profit_0

# DP, MLE
class Solution(object):
    def get_max_profit(self, i):
        if i >= self.N:
            return 0
        if self.max_profit[i] != -1:
            return self.max_profit[i]

        local_min = self.prices[i]
        profit = 0
        # for j > i, if I buy at price i and sell at price j, what's the max profit
        for j in range(i + 1, self.N):
            if self.prices[j] < local_min:
                local_min = self.prices[j]
                break
            elif self.prices[j] - local_min <= self.fee:
                pass
            else:
                current_profit = self.prices[j] - local_min - self.fee
                profit = max(profit, current_profit + self.get_max_profit(j + 1))

        self.max_profit[i] = profit
        return profit

    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0

        self.N = len(prices)
        self.prices = prices
        self.fee = fee
        self.max_profit = [-1] * self.N # max_profit[i]: max profit I can make from prices[i:]

        return self.get_max_profit(0)

# recursion, TLE
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0

        total_profit = 0
        N = len(prices)
        local_min = prices[0]

        for i in range(N):
            if prices[i] < local_min:
                local_min = prices[i]
            elif prices[i] - local_min <= fee:
                pass
            else:
                current_profit = prices[i] - local_min - fee
                total_profit = max(total_profit, current_profit + self.maxProfit(prices[i + 1:], fee))

        return total_profit