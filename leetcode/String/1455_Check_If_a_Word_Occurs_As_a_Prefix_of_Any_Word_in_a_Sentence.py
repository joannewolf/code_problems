class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        words = sentence.split(' ')
        N = len(words)
        K = len(searchWord)
        for i in range(N):
            if words[i][:K] == searchWord:
                return i + 1

        return -1
