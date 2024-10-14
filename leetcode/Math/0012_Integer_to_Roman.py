class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ''
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        M = ['', 'M', 'MM', 'MMM']

        result = I[num % 10] + result
        num //= 10
        result = X[num % 10] + result
        num //= 10
        result = C[num % 10] + result
        num //= 10
        result = M[num % 10] + result

        return result
