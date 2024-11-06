class Solution(object):
    def canSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        bits = []
        for num in nums:
            val = num
            count = 0
            while num != 0:
                count += num % 2
                num //= 2
            bits.append(count)

        N = len(nums)
        new_nums = []
        current_bit = bits[0]
        left = 0
        for i in range(1, N):
            if bits[i] == current_bit:
                pass
            else:
                new_nums.extend(sorted(nums[left: i]))
                current_bit = bits[i]
                left = i
        new_nums.extend(sorted(nums[left: N]))

        for i in range(N - 1):
            if new_nums[i] > new_nums[i+1]:
                return False
        return True
