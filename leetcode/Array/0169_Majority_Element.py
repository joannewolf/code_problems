# O(N), O(N) space
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1

        for k, v in num_dict.items():
            if v > N // 2:
                return k

# O(N), O(1) space
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = None
        count = 0

        for n in nums:
            if count == 0:
                result = n

            if n == result:
                count += 1
            else:
                count -= 1

        return result
