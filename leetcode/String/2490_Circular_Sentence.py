class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        words = sentence.split(' ')
        N = len(words)
        for i in range(N - 1):
            if words[i][-1] != words[i+1][0]:
                return False

        if words[-1][-1] != words[0][0]:
            return False

        return True
