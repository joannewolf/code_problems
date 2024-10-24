# O(N), O(N) space
class Solution(object):
    def singleNumber(self, nums):
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

        return list(num_set)[0]

# O(N), O(1) space
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num

        return result
