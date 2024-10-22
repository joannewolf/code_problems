class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        N = len(s)
        flag = N - 1
        while s[flag] == ' ':
            flag -= 1
        while flag >= 0 and s[flag] != ' ':
            count += 1
            flag -= 1
        return count
