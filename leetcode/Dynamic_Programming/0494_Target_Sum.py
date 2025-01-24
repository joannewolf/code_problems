class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = {0: 1} # dp[i]: the number of ways to sum to i

        for num in nums:
            next_dp = {}
            for key, val in dp.items():
                if key - num in next_dp:
                    next_dp[key - num] += val
                else:
                    next_dp[key - num] = val

                if key + num in next_dp:
                    next_dp[key + num] += val
                else:
                    next_dp[key + num] = val

            dp = next_dp

        return dp[target] if target in dp else 0
