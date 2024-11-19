class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        nums.sort()
        count = 0
        right = N - 1
        for left in range(N):
            while right > left and nums[left] + nums[right] >= target:
                right -= 1
            if right < left:
                right = left

            count += (right - left)

        return count
