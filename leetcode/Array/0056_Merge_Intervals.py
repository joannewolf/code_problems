class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        N = len(intervals)
        intervals.sort(key=lambda interval: interval[0])

        for i in range(N):
            if not result:
                result.append(intervals[i])
            elif result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
            else:
                result[-1][1] = max(result[-1][1], intervals[i][1])

        return result
