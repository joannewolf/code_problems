class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lcp = ''
        N = len(strs)

        # find minimum str len
        min_strlen = 210
        for s in strs:
            min_strlen = min(min_strlen, len(s))
        if min_strlen == 0:
            return ''

        for i in range(min_strlen):
            char = strs[0][i]
            all_same = True
            for j in range(1, N):
                if strs[j][i] != char:
                    all_same = False
                    break

            if all_same:
                lcp += char
            else:
                break

        return lcp
