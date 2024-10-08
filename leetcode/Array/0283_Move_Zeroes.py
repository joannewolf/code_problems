class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        count = 0
        i = 0
        while count < N:
            if nums[i] != 0:
                i += 1
            else:
                del nums[i]
                nums.append(0)
            count += 1
