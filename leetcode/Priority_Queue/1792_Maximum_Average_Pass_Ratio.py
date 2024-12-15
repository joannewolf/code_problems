class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        import heapq
        N = len(classes)
        queue = []
        for [above, below] in classes:
            above = float(above)
            below = float(below)
            # heapq only support min-heap, so make the value negative to implement max-heap
            score = -(((above + 1) / (below + 1)) - (above / below))
            queue.append((score, above, below))

        heapq.heapify(queue)

        for _ in range(extraStudents):
            (_, above, below) = heapq.heappop(queue)
            above += 1
            below += 1
            new_score = -(((above + 1) / (below + 1)) - (above / below))
            heapq.heappush(queue, (new_score, above, below))

        return sum([above / below for _, above, below in queue]) / N
