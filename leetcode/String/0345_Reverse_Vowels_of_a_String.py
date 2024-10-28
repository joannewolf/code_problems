class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiouAEIOU'
        vowel_index = []
        s = list(s)
        for i, char in enumerate(s):
            if char in vowels:
                vowel_index.append(i)

        N = len(vowel_index)
        for i in range(N // 2):
            s[vowel_index[i]], s[vowel_index[N - 1 - i]] = s[vowel_index[N - 1 - i]], s[vowel_index[i]]

        return ''.join(s)
