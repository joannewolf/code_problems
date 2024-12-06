class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        banned = set(banned)
        count = 0
        sum = 0
        for i in range(1, n + 1):
            if i not in banned:
                if sum + i <= maxSum:
                    sum += i
                    count += 1
                else:
                    break

        return count
