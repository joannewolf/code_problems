class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        num_set = set(nums)
        result = -1

        # try each num as streak start
        for num in nums:
            count = 1
            current = num
            while current * current in num_set:
                count += 1
                current = current * current

            if count >= 2:
                result = max(result, count)

        return result
