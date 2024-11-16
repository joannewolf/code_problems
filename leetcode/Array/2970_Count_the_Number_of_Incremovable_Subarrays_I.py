class Solution(object):
    def incremovableSubarrayCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1

        N = len(nums)
        count = 0
        left_increasing = [False] * N # left_increasing[i]: is nums[:i+1] increasing
        right_increasing = [False] * N # right_increasing[i]: is nums[i:] increasing
        left_increasing[0] = True
        for i in range(1, N):
            if nums[i - 1] < nums[i]:
                left_increasing[i] = True
            else:
                break
        right_increasing[N - 1] = True
        for i in range(N - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                right_increasing[i] = True
            else:
                break

        for i in range(N):
            for j in range(i, N):
                if i == 0 and j == N - 1:
                    count += 1
                elif i == 0 and j < N - 1 and right_increasing[j + 1]:
                    count += 1
                elif i > 0 and j == N - 1 and left_increasing[i - 1]:
                    count += 1
                elif (i > 0 and j < N - 1 and
                    left_increasing[i - 1] and right_increasing[j + 1] and nums[i - 1] < nums[j + 1]):
                    count += 1

        return count
