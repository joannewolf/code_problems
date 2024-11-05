class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        char_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        if not digits:
            return []

        result = ['']
        for digit in digits:
            next_result = []
            for char in char_dict[digit]:
                for str in result:
                    next_result.append(str + char)

            result = next_result
        return result
