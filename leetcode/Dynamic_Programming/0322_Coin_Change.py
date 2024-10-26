class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        INT_MAX = 100000
        coins.sort()
        dp = [INT_MAX] * (amount + 1) # dp[i] means the min coins to make up i dollars
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                else:
                    break

        if dp[amount] == INT_MAX:
            return -1
        else:
            return dp[amount]
