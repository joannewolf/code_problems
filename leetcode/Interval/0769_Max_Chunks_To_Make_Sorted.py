class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        N = len(arr)
        # if val i is at arr[j], it must belong to partition cover [i..j] or [j..i]
        # make all val and arr index as intervals
        # find the max non-overlapping group of intervals
        intervals = []
        for i, num in enumerate(arr):
            intervals.append([min(i, num), max(i, num)])

        intervals.sort()
        count = 0
        current_interval = [-1, -1]
        for i in range(N):
            if current_interval[1] < intervals[i][0]:
                count += 1
                current_interval = intervals[i]
            else:
                current_interval[1] = max(current_interval[1], intervals[i][1])

        return count
