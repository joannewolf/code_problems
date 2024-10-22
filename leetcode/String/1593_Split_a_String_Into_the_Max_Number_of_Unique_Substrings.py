class Solution(object):
    # return all valid unique split substrs, list of sets
    def splitStr(self, s):
        N = len(s)
        if N == 0:
            return []

        result = [set([s])]
        for i in range(1, N):
            current_str = s[:i]
            all_substr_result = self.splitStr(s[i:])
            for substr_result in all_substr_result:
                if current_str not in substr_result:
                    substr_result.add(current_str)
                    result.append(substr_result)

        return result

    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_count = 1
        all_substr_result = self.splitStr(s)
        for substr_result in all_substr_result:
            max_count = max(max_count, len(substr_result))

        return max_count
