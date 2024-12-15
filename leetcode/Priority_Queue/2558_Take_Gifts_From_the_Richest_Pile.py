class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        from math import sqrt
        # heapq only support min-heap, so make the value negative to implement max-heap
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            pile = heapq.heappop(gifts)
            remain = int(sqrt(-pile))
            heapq.heappush(gifts, -remain)

        return sum(gifts)