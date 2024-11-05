class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if x == 1 or n == 0:
            return 1

        abs_n = abs(n)
        multiples = [1, x] # multiples[i] = x^(2^i)
        power = 2
        while power <= abs_n:
            multiples.append(multiples[-1] * multiples[-1])
            power *= 2

        result = 1
        N = len(multiples)
        power //= 2
        for i in range(N-1, 0, -1):
            if power <= abs_n:
                result *= multiples[i]
                abs_n -= power

            power //= 2

        if n >= 0:
            return result
        else:
            return 1 / result
