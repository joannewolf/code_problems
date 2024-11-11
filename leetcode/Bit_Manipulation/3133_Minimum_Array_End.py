class Solution(object):
    def minEnd(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        # AND result must be x, so all nums should have same bit 1 as x
        # for the rest bit 0 space, use (n - 1) to fill it
        num = n - 1
        bit_index = 0
        while num > 0:
            if not x & (1 << bit_index):
                x += (num & 1) << bit_index
                num >>= 1

            bit_index += 1

        return x
