class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        nums = nums + nums[:-1]
        result = [-1] * N
        stack = []
        for i in range(2 * N - 1):
            while stack and nums[stack[-1] % N] < nums[i % N]:
                result[stack[-1] % N] = nums[i % N]
                stack.pop()

            stack.append(i % N)

        return result
