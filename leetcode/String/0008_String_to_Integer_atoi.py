class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)
        N = len(s)
        result = 0
        sign = 1
        flag = 0

        while flag < N and s[flag] == ' ':
            flag += 1

        if flag < N and s[flag] == '-':
            sign = -1
            flag += 1
        elif flag < N and s[flag] == '+':
            flag += 1

        while flag < N and s[flag].isdigit():
            result *= 10
            result += int(s[flag])
            flag += 1

        result *= sign

        if result > INT_MAX:
            result = INT_MAX
        elif result < INT_MIN:
            result = INT_MIN

        return result
