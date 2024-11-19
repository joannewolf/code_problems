# O(N^2)
class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr = [-1] + arr + [-1]
        N = len(arr)
        result = 0
        for i in range(1, N - 1):
            # take arr[i] as peak, check the logest mountain
            left, right = i, i
            for left in range(i, 0, -1):
                if arr[left - 1] >= arr[left]:
                    break
            for right in range(i, N - 1):
                if arr[right] <= arr[right + 1]:
                    break

            if left != i and right != i:
                result = max(result, right - left + 1)

        return result

# O(N), O(N) space
class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        N = len(arr)
        left = [0] * N # left[i]: the longest increasing subarray until arr[i-1]
        right = [0] * N # right[i]: the longest decreasing subarray from arr[i+1]

        count = 0
        for i in range(1, N):
            if arr[i] > arr[i - 1]:
                count += 1
                left[i] = count
            else:
                count = 0

        count = 0
        for i in range(N - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                count += 1
                right[i] = count
            else:
                count = 0

        result = 0
        for i in range(N):
            if left[i] != 0 and right[i] != 0:
                result = max(result, left[i] + right[i] + 1)

        return result

# O(N), O(1) space
class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        N = len(arr)
        result = 0
        left, right = 0, 0

        # a mountain can only start after the previous one ends
        # so find mountain one by one from left to right
        while left < N:
            right = left
            climb_up, climb_down = False, False
            while right < N - 1 and arr[right] < arr[right + 1]:
                climb_up = True
                right += 1
            while right < N - 1 and arr[right] > arr[right + 1]:
                climb_down = True
                right += 1

            if climb_up and climb_down:
                result = max(result, right - left + 1)

            left = max(right, left + 1)

        return result
