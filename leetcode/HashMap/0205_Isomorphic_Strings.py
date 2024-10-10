class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        N = len(s)
        # check same char in s must map to same char in t
        s_dict = {}
        for i in range(N):
            if s[i] not in s_dict:
                s_dict[s[i]] = t[i]
            elif s_dict[s[i]] != t[i]:
                return False

        # check if values of s_dict are distinct
        if len(s_dict.values()) != len(set(s_dict.values())):
            return False

        return True
