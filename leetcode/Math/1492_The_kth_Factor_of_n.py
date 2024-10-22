class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        import math
        factors = []
        # add left half of factors
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                factors.append(i)

        if factors[-1] * factors[-1] == n:
            N = len(factors) * 2 - 1
        else:
            N = len(factors) * 2

        if N < k:
            return -1
        elif k <= len(factors):
            return factors[k - 1]
        else:
            if factors[-1] * factors[-1] == n:
                index = k - len(factors) + 1
            else:
                index = k - len(factors)
            return n // factors[-index]
