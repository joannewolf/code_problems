# O(N^2), TLE
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        N = len(height)
        result = 0
        for i in range(N):
            for j in range(i + 1, N):
                result = max(result, min(height[i], height[j]) * (j - i))

        return result

# O(N)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        N = len(height)
        left, right = 0, N - 1
        result = 0
        while left < right:
            if height[left] < height[right]:
                result = max(result, height[left] * (right - left))
                left += 1
            else:
                result = max(result, height[right] * (right - left))
                right -= 1

        return result
