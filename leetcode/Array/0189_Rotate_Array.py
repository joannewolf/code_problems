class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k %= N
        # for i in range(k):
        #     nums.insert(0, nums.pop())
        for i in range(N - k):
            nums.append(nums.pop(0))
