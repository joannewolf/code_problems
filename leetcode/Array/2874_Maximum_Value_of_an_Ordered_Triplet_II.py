class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        INT_MAX = 1e07
        N = len(nums)
        max_left = [0] * N # max_left[i]: max(nums[:i+1])
        max_right = [0] * N # max_right[i]: max(nums[i:])

        local_max = 0
        for i in range(N):
            local_max = max(local_max, nums[i])
            max_left[i] = local_max
        local_max = 0
        for i in range(N - 1, -1, -1):
            local_max = max(local_max, nums[i])
            max_right[i] = local_max

        result = 0
        for j in range(1, N - 1):
            num_i = max_left[j - 1]
            num_k = max_right[j + 1]
            result = max(result, (num_i - nums[j]) * num_k)

        return result