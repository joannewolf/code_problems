# BFS
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        N = len(arr)
        checked = set() # prevent cycle
        current_steps = set([start])
        while current_steps:
            next_steps = set()
            for pos in current_steps:
                if arr[pos] == 0:
                    return True
                if pos - arr[pos] >= 0 and pos - arr[pos] not in checked:
                    next_steps.add(pos - arr[pos])
                if pos + arr[pos] <= N - 1 and pos + arr[pos] not in checked:
                    next_steps.add(pos + arr[pos])
                checked.add(pos)

            current_steps = next_steps

        return False