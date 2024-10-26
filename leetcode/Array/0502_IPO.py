class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        projects = list(zip(profits, capital))
        projects.sort(key=lambda val: val[1]) # sort by capital ascending

        import heapq
        N = len(projects)
        # greedily find the current max-profit project at each round
        flag = 0
        candidates = []
        for _ in range(k):
            while flag < N and projects[flag][1] <= w:
                # heapq only support min-heap, so make the value negative to implement max-heap
                heapq.heappush(candidates, -projects[flag][0])
                flag += 1

            if not candidates:
                break

            w += -heapq.heappop(candidates)

        return w
