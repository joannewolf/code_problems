class Solution(object):
    def maximumBeauty(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        N = len(nums)
        intervals = [[num - k, num + k] for num in nums]
        intervals.sort()

        # find the max interval overlap
        max_overlap = 1
        left = 0
        for right in range(1, N):
            while intervals[left][1] < intervals[right][0]:
                left += 1

            max_overlap = max(max_overlap, right - left + 1)

        return max_overlap
