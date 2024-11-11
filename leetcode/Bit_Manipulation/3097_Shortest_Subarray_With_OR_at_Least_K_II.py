# O(N)
class Solution(object):
    def addNumToBits(self, bits, num, sign):
        N = len(bits)
        for i in range(N):
            bits[i] += sign * (num & (1 << i))

    def bitsToNum(self, bits):
        result = 0
        N = len(bits)
        for i in range(N):
            if bits[i] > 0:
                result |= (1 << i)

        return result

    def minimumSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MAX_BITS = 31
        N = len(nums)
        min_len = N + 1
        bits = [0] * MAX_BITS
        left, right = 0, 0

        # OR result must >= operands
        while right < N:
            self.addNumToBits(bits, nums[right], 1)

            while left <= right and self.bitsToNum(bits) >= k:
                min_len = min(min_len, right - left + 1)
                # remove left num
                self.addNumToBits(bits, nums[left], -1)
                left += 1

            right += 1

        return min_len if min_len != N + 1 else -1


# O(N^2), TLE
class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if max(nums) >= k:
            return 1

        N = len(nums)
        # dp[i]: with current n, subarray len = n-1 until nums[i] OR result, i.e. nums[i-n+2:i+1]
        dp = list(nums)
        for n in range(2, N + 1):
            new_dp = [0] * N
            for i in range(N - 1, n - 2, -1):
                new_dp[i] = nums[i] | dp[i - 1]
                if new_dp[i] >= k:
                    return n

            dp = new_dp

        return -1
