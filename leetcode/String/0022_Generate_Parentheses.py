class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return ['']

        result = set()
        subresults = self.generateParenthesis(n - 1)
        for subresult in subresults:
            # insert '()' in all possible positions
            for i in range(2 * n - 1):
                result.add(subresult[:i] + '()' + subresult[i:])

        return list(result)
