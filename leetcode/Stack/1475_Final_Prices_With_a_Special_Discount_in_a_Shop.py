class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        N = len(prices)
        result = [None] * N
        min_prices_stack = []
        for i in range(N - 1, -1, -1):
            while min_prices_stack and min_prices_stack[-1] > prices[i]:
                min_prices_stack.pop()

            if min_prices_stack:
                result[i] = prices[i] - min_prices_stack[-1]
            else:
                result[i] = prices[i]

            min_prices_stack.append(prices[i])

        return result
