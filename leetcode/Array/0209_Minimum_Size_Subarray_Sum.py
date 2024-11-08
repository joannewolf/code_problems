class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        count = N + 1
        left, right = 0, 0
        num_sum = 0
        while right < N:
            num_sum += nums[right]
            if num_sum >= target:
                while left <= right and num_sum >= target:
                    count = min(count, right - left + 1)
                    num_sum -= nums[left]
                    left += 1

            right += 1

        if count == N + 1:
            return 0
        else:
            return count
