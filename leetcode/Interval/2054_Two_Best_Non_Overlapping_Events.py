class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        N = len(events)
        events.sort(key=lambda interval: interval[0])
        max_right_val = [0] * N # max_right_val[i]: max value of events[i:]

        max_val = 0
        for i in range(N - 1, -1, -1):
            max_val = max(max_val, events[i][2])
            max_right_val[i] = max_val

        max_total_val = 0
        for i in range(N):
            left, right = i + 1, N - 1
            while left <= right:
                mid = (left + right) // 2
                if events[mid][0] <= events[i][1]:
                    left = mid + 1
                else:
                    right = mid - 1
            # final L is min element index which > target
            if left == N:
                max_total_val = max(max_total_val, events[i][2])
            else:
                max_total_val = max(max_total_val, events[i][2] + max_right_val[left])

        return max_total_val