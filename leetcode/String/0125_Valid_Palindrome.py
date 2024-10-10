class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean_s = ''
        for char in s:
            if char.isalnum():
                if char.isupper():
                    char = char.lower()
                clean_s += char

        N = len(clean_s)
        l, r = 0, N - 1
        while l < r:
            if clean_s[l] != clean_s[r]:
                return False
            l += 1
            r -= 1

        return True
