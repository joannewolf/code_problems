class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        N = len(digits)
        overflow = 0
        digits[-1] += 1
        for i in range(N-1, -1, -1):
            digits[i] += overflow
            if digits[i] > 9:
                overflow = digits[i] // 10
                digits[i] %= 10
            else:
                overflow = 0
                break

        if overflow != 0:
            digits.insert(0, overflow)
        return digits
