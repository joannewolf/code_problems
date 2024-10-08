class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }
        num = 0
        N = len(s)
        i = 0
        while i < N:
            if i == N - 1 or s[i:i+2] not in digits:
                num += digits[s[i]]
                i += 1
            elif s[i:i+2] in digits:
                num += digits[s[i:i+2]]
                i += 2

        return num
