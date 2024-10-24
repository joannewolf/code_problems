class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = 0
        # XOR all the nums and find out the XOR result of the two answers
        for num in nums:
            diff ^= num

        # assume bit i is 1 in diff, it means bit i of two answers are different
        # categorize all nums into bit i 0 and 1, and XOR to get each answer
        diff &= -diff # this will get the last bit 1 of diff
        result = [0, 0]
        for num in nums:
            if num & diff:
                result[0] ^= num
            else:
                result[1] ^= num

        return result
