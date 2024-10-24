class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        num_sum = N * (N + 1) // 2
        return num_sum - sum(nums)
