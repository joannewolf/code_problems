# O(N^2), DP
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        result = 1
        dp = [1] * N # dp[i]: the max len of increasing sequence until nums[i], including nums[i]

        for i in range(1, N):
            for j in range(i):
                if nums[i] > nums[j]: # can append nums[i] in increasing sequence ends at nums[j]
                    dp[i] = max(dp[i], dp[j] + 1)

            result = max(result, dp[i])

        return result

# O(NlogN), binary search
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        IS = [nums[0]]

        for i in range(1, N):
            # find nums[i] should be inserted in which position in increasing subsequence
            left, right = 0, len(IS) - 1
            while left <= right:
                mid = (left + right) // 2
                if IS[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid - 1
            # the final L is the index of first occurrence or index for inserting
            if left < len(IS):
                IS[left] = nums[i]
            else:
                IS.append(nums[i])

        return len(IS)
