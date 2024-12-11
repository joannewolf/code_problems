class Solution(object):
    def isArraySpecial(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        N = len(nums)
        result = []
        prefix_count = [0] # prefix_count[i]: # of same parity pair in nums[:i+1]
        count = 0
        for i in range(1, N):
            if nums[i] % 2 == nums[i - 1] % 2:
                count += 1
            prefix_count.append(count)

        for [start, end] in queries:
            same_parity_count = prefix_count[end] - prefix_count[start]
            result.append((same_parity_count == 0))

        return result
