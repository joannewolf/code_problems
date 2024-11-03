class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s += '.'
        N = len(s)
        result = ''

        char_count = 1
        for i in range(N):
            if i > 0 and s[i] == s[i - 1]:
                char_count += 1
            else:
                if char_count >= 2:
                    result += s[i - 1]
                result += s[i]
                char_count = 1

        return result[:-1] # remove period
