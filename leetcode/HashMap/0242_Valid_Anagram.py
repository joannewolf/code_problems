class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_dict_s = {}
        char_dict_t = {}
        for char in s:
            if char not in char_dict_s:
                char_dict_s[char] = 1
            else:
                char_dict_s[char] += 1
        for char in t:
            if char not in char_dict_t:
                char_dict_t[char] = 1
            else:
                char_dict_t[char] += 1

        if set(char_dict_s.keys()) != set(char_dict_t.keys()):
            return False

        for char in char_dict_s.keys():
            if char_dict_s[char] != char_dict_t[char]:
                return False

        return True
