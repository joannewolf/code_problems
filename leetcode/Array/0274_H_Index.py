# O(NlogN)
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        citations.sort(reverse=True)
        result = 0
        for i in range(N):
            result = max(result, min(i + 1, citations[i]))
        return result
