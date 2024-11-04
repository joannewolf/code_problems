class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        result = 0
        char_dict = set()
        start, end = 0, 0
        while end < N:
            if s[end] not in char_dict:
                char_dict.add(s[end])
                end += 1
            else:
                result = max(result, len(char_dict))
                for i in range(start, end):
                    if s[i] == s[end]:
                        start = i + 1
                        break
                    else:
                        char_dict.remove(s[i])
                end += 1

        result = max(result, len(char_dict))

        return result
