class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        N, K = len(haystack), len(needle)
        for i in range(N - K + 1):
            if haystack[i:i+K] == needle:
                return i

        return -1
