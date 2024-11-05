class Solution(object):
    def compressedString(self, word):
        """
        :type word: str
        :rtype: str
        """
        word += '.' # for triggering last compression
        N = len(word)
        current_char = word[0]
        count = 1
        result = []
        for i in range(1, N):
            if count == 9 or word[i] != current_char:
                result.append(str(count) + current_char)
                current_char = word[i]
                count = 1
            elif word[i] == current_char:
                count += 1

        return ''.join(result)
