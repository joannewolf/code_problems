# O(N), O(N) space
class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set()
        for num in nums:
            if num not in num_set:
                num_set.add(num)
            else:
                num_set.remove(num)
        # num_set now only have nums which appears once
        num_set = set(nums).difference(num_set)

        result = 0
        for num in num_set:
            result ^= num

        return result

# O(N), O(1) space
# since 1 <= nums[i] <= 50, user 50 bits ~= one int to represent each num
class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        seen = 0
        for num in nums:
            if seen & (1 << num):
                result ^= num
            else:
                seen |= (1 << num)

        return result
