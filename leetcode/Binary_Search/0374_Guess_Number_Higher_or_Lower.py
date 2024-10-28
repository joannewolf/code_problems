# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            middle = (left + right) // 2
            ans = guess(middle)
            if ans == 0:
                return middle
            elif ans > 0:
                left = middle + 1
            else:
                right = middle - 1

        return left
