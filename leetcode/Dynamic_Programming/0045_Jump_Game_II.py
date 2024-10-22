# O(N^2), DP
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        INT_MAX = 100000
        N = len(nums)
        dp = [INT_MAX] * N # dp[i] means the minimum steps from index i to last index
        dp[-1] = 0

        for i in range(N - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if i + j >= N:
                    break
                dp[i] = min(dp[i], dp[i + j] + 1)

        return dp[0]

# O(N), sliding window
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        current_end = 0 # the max index we can jump from current
        farthest = 0 # next farthest index we can reach after jumping from current
        jumps = 0

        for i in range(N - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end: # have checked all possible next jump
                jumps += 1
                current_end = farthest
                if current_end >= N - 1:
                    break

        return jumps
