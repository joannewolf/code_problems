class Solution(object):
    # whether can divide into new nums <= k
    def canOperate(self, nums, maxOperations, k):
        import math
        count = sum([math.ceil(float(num) / k) for num in nums])
        return count - len(nums) <= maxOperations

    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        result = -1
        left, right = 1, max(nums)
        # when feeding array element to function will return [False, False, ..., True, True]
        # return first element that function return True
        while left <= right:
            mid = (left + right) // 2
            if self.canOperate(nums, maxOperations, mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result