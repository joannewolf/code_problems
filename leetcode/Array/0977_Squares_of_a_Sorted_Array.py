# O(NlogN)
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i, val in enumerate(nums):
            nums[i] = val * val

        nums.sort()
        return nums

# O(N)
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i, val in enumerate(nums):
            nums[i] = abs(val)
        # find the minimum abs num
        N = len(nums)
        start = N - 1
        for i in range(N - 1):
            if nums[i] < nums[i + 1]:
                start = i
                break

        result = [nums[start] * nums[start]]
        left, right = start - 1, start + 1
        while left >= 0 or right < N:
            if left < 0:
                result.append(nums[right] * nums[right])
                right += 1
            elif right == N:
                result.append(nums[left] * nums[left])
                left -= 1
            elif nums[left] <= nums[right]:
                result.append(nums[left] * nums[left])
                left -= 1
            else:
                result.append(nums[right] * nums[right])
                right += 1

        return result
