# O(N) space
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        words = [w for w in words if w != '']
        return ' '.join(words[::-1])

# O(1) space, in-place
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s) # convert str to char list
        # trim extra spaces
        i = 0
        while i < len(s):
            if i != len(s) - 1 and s[i] == ' ' and s[i + 1] == ' ':
                del s[i + 1]
            else:
                i += 1
        if s[0] == ' ':
            del s[0]
        if s[-1] == ' ':
            del s[-1]

        N = len(s)
        s = s[::-1] # reverse whold sentence
        l, r = 0, N - 1
        while l < N:
            for i in range(l + 1, N):
                if s[i] == ' ':
                    r = i - 1
                    break
            # reverse each word
            n = r - l + 1
            for i in range(n // 2):
                s[l + i], s[r - i] = s[r - i], s[l + i]

            l = r + 2
            r = N - 1

        return ''.join(s)
