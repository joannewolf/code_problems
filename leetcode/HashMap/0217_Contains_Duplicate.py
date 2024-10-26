class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_set = set()
        for num in nums:
            if num not in num_set:
                num_set.add(num)
            else:
                return True

        return False
