class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        slow, fast = 0, 0
        count = 0
        while fast < N:
            if nums[fast] == nums[slow]:
                count += 1
                fast += 1
            else:
                if count >= 2:
                    nums[slow+1] = nums[slow]
                    slow += 2
                else:
                    slow += 1
                nums[slow] = nums[fast]
                count = 1
                fast += 1

        if count >= 2:
            nums[slow+1] = nums[-1]
            return slow + 2
        else:
            return slow + 1
