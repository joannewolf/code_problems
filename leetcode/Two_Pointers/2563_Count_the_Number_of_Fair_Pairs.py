class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        N = len(nums)
        count = 0
        nums.sort()
        right_lower, right_upper = N - 1, N - 1
        for left in range(N):
            while right_upper >= left and nums[left] + nums[right_upper] > upper:
                right_upper -= 1
            if right_upper < left:
                right_upper = left

            while right_lower >= left and nums[left] + nums[right_lower] >= lower:
                right_lower -= 1
            if right_lower < left:
                right_lower = left

            count += (right_upper - right_lower)

        return count
