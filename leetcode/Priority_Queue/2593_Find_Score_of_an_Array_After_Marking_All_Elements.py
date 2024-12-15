class Solution(object):
    def findScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq
        score = 0
        checked_index = set()
        queue = [(num, i) for (i, num) in enumerate(nums)]
        heapq.heapify(queue)
        while queue:
            (min_val, i) = heapq.heappop(queue)
            if i not in checked_index:
                score += min_val
                checked_index.add(i)
                checked_index.add(i - 1)
                checked_index.add(i + 1)

        return score
