class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ''
        N, M = len(word1), len(word2)
        i, j = 0, 0
        flag = 1
        while i < N or j < M:
            if i == N:
                result += word2[j:]
                break
            elif j == M:
                result += word1[i:]
                break
            elif flag == 1:
                result += word1[i]
                i += 1
                flag = 2
            else:
                result += word2[j]
                j += 1
                flag = 1

        return result
