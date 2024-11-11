class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        N = len(nums)
        # cuz nums[i] < 2^maximumBit, bits count is <= maximumBit
        num_bits = [0] * maximumBit
        for num in nums:
            for i in range(maximumBit):
                if num == 0:
                    break
                num_bits[i] += num & 1
                num >>= 1

        # to max XOR result, all bits count must be odd number
        result = []
        for i in range(N):
            k = 0
            for j in range(maximumBit):
                if num_bits[j] & 1 == 0:
                    k += (1 << j)
            result.append(k)
            # remove last num
            last_num = nums[N - 1 - i]
            for j in range(maximumBit):
                if last_num == 0:
                    break
                num_bits[j] -= last_num & 1
                last_num >>= 1
        return result
