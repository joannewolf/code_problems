class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        import heapq
        N = len(nums)
        queue = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(queue)

        for _ in range(k):
            (min_val, i) = heapq.heappop(queue)
            heapq.heappush(queue, (min_val * multiplier, i))

        result = [0] * N
        for (val, i) in queue:
            result[i] = val

        return result
