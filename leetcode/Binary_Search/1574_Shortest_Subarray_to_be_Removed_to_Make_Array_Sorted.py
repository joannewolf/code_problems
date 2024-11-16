# O(NlogN)
class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        N = len(arr)
        # I: arr[:I+1] is the max increasing prefix subarray
        # J: arr[J:] is the max increasing suffix subarray
        I, J = 0, N - 1
        for i in range(1, N):
            if arr[i - 1] <= arr[i]:
                I = i
            else:
                break
        for j in range(N - 2, -1, -1):
            if arr[j] <= arr[j + 1]:
                J = j
            else:
                break

        # no need to remove any subarray
        if I == N - 1:
            return 0

        # I < J
        min_len = min(N - (I + 1), J) # either keep only prefix or suffix subarray
        # for prefix subarray arr[:i+1], find the inserting point in suffix subarray
        for i in range(I + 1):
            left, right = J, N - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] < arr[i]:
                    left = mid + 1
                else:
                    right = mid - 1
            # final L is min element index which >= target, i.e. cut subarray[i+1: left]
            min_len = min(min_len, left - (i + 1))

        return min_len

# O(N^2), TLE
class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        N = len(arr)
        left_increasing = [False] * N # left_increasing[i]: is arr[:i+1] increasing
        right_increasing = [False] * N # right_increasing[i]: is arr[i:] increasing
        left_increasing[0] = True
        for i in range(1, N):
            if arr[i - 1] <= arr[i]:
                left_increasing[i] = True
            else:
                break
        right_increasing[N - 1] = True
        for i in range(N - 2, -1, -1):
            if arr[i] <= arr[i + 1]:
                right_increasing[i] = True
            else:
                break

        # no need to remove any subarray
        if left_increasing[N - 1]:
            return 0
        min_len = N - 1
        for i in range(N):
            for j in range(i, N):
                if i == 0 and j < N - 1 and right_increasing[j + 1]:
                    min_len = min(min_len, j - i + 1)
                elif i > 0 and j == N - 1 and left_increasing[i - 1]:
                    min_len = min(min_len, j - i + 1)
                elif (i > 0 and j < N - 1 and
                    left_increasing[i - 1] and right_increasing[j + 1] and arr[i - 1] <= arr[j + 1]):
                    min_len = min(min_len, j - i + 1)

        return min_len
