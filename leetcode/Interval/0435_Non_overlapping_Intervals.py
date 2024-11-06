class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        N = len(intervals)
        # sort by x_end
        intervals.sort(key=lambda interval: interval[1])
        result = 0
        left = 0
        for i in range(1, N):
            if intervals[left][1] <= intervals[i][0]:
                left = i
            else:
                result += 1

        return result
