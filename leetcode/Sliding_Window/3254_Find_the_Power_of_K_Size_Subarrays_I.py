class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        N = len(nums)
        # list of pair [start, len], meaning nums[start: start+len] is consecutive and ascending
        increasing_subarrays = [[0, 1]]
        for i in range(1, N):
            if nums[i] == nums[i - 1] + 1:
                increasing_subarrays[-1][1] += 1
            else:
                increasing_subarrays.append([i, 1])

        result = []
        flag = 0
        for i in range(N - k + 1):
            start, n = increasing_subarrays[flag]
            if i >= start + n:
                flag += 1
                start, n = increasing_subarrays[flag]

            if i + k - 1 < start + n:
                result.append(nums[i] + k - 1)
            else:
                result.append(-1)

        return result
