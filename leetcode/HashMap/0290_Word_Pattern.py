class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(' ')
        if len(pattern) != len(words):
            return False

        N = len(pattern)
        dict = {}
        for i in range(N):
            if pattern[i] not in dict:
                dict[pattern[i]] = words[i]
            elif dict[pattern[i]] != words[i]:
                return False

        # check if duplicate dict value
        if len(dict.values()) != len(set(dict.values())):
            return False

        return True