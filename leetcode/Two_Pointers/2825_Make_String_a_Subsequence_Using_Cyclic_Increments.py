class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        N, M = len(str1), len(str2)
        str1 = [ord(char) - ord('a') for char in str1]
        str2 = [ord(char) - ord('a') for char in str2]
        j = 0
        for i in range(N):
            if str1[i] == str2[j] or (str1[i] + 1) % 26 == str2[j]:
                j += 1
            if j == M:
                return True

        return False
