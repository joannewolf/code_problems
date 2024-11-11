class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        MAX_BIT = 25 # cuz candidates[i] <= 10^7, log2(10^7) ~= 23.25..
        # to get AND result > 0, at least one bit 1 must overlap
        # so count all candidates' bit 1s and find the most overlapped bit 1
        bit_count = [0] * MAX_BIT # bit_count[i]: the candidate count which have bit i = 1
        for num in candidates:
            for i in range(MAX_BIT):
                if num == 0:
                    break
                bit_count[i] += num & 1
                num >>= 1

        return max(bit_count)
