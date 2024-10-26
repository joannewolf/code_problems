class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        N, M = len(str1), len(str2)
        flag = 0
        while flag < N and flag < M and str1[flag] == str2[flag]:
            flag += 1
        lcp = str1[:flag]
        K = len(lcp)
        for k in range(K, 0, -1):
            if (N % k == 0 and M % k == 0 and
                lcp[:k] * (N // k) == str1 and lcp[:k] * (M // k) == str2):
                return lcp[:k]

        return ''
