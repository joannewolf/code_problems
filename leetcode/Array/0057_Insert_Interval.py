from unittest import result


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        N = len(intervals)
        # binary search to find insert point
        left, right = 0, N - 1
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < newInterval[0]:
                left = mid + 1
            else:
                right = mid - 1

        # final left is the insert point
        intervals.insert(left, newInterval)
        N += 1
        if left == 0 or intervals[left-1][1] < intervals[left][0]:
            flag = left
        else:
            flag = left - 1

        # merge intervals
        while flag < N:
            if flag == N - 1 or intervals[flag][1] < intervals[flag+1][0]:
                break

            intervals[flag][0] = min(intervals[flag][0], intervals[flag+1][0])
            intervals[flag][1] = max(intervals[flag][1], intervals[flag+1][1])
            del intervals[flag+1]
            N -= 1

        return intervals
