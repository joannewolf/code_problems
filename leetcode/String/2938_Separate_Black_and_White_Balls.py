class Solution(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        result = 0
        white_count = 0
        # every '1' has to at least swap with '0' on its right side
        for i in range(N - 1, -1, -1):
            if s[i] == '0':
                white_count += 1
            elif s[i] == '1':
                result += white_count

        return result
