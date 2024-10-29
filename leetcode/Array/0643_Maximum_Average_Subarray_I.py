class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        N = len(nums)
        sliding_sum = sum(nums[:k])
        max_sum = sliding_sum

        for i in range(N - k):
            sliding_sum -= nums[i]
            sliding_sum += nums[i + k]
            max_sum = max(max_sum, sliding_sum)

        return float(max_sum) / k
