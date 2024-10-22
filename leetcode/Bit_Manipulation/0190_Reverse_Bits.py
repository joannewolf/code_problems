class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for _ in range(32):
            bit = n % 2
            result = result * 2 + bit
            n //= 2
        return result
