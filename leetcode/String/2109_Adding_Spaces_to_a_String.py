class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        N = len(s)
        K = len(spaces)
        s = list(s)
        result = []
        k = 0
        for i in range(N):
            if k < K and i == spaces[k]:
                result.append(' ')
                k += 1
            result.append(s[i])

        result = ''.join(result)
        return result
