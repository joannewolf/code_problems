class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        N = len(s)
        # try each char as palindrome center
        for i in range(N):
            # odd center palindrome
            left, right = i - 1, i + 1
            while left >= 0 and right <= N - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > len(result):
                result = s[left + 1:right]

            # even center palindrome
            left, right = i, i + 1
            while left >= 0 and right <= N - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > len(result):
                result = s[left + 1:right]

        return result
