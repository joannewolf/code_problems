# recursion
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        N = len(nums)
        if N == 0:
            return [[]]

        nums.sort()
        result = []
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            subresults = self.permuteUnique(nums[:i] + nums[i+1:])
            for subresult in subresults:
                result.append(subresult + [nums[i]])

        return result
