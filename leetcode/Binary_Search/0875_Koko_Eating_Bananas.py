class Solution(object):
    # whether can distribute <= h hours
    def canFinish(self, k):
        import math
        count = 0
        for pile in self.piles:
            count += math.ceil(float(pile) / k)

        return count <= self.h

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        self.piles = piles
        self.h = h
        result = -1
        left, right = 1, max(piles)
        # when feeding array element to function will return [False, False, ..., True, True]
        # return first element that function return True
        while left <= right:
            mid = (left + right) // 2
            if self.canFinish(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
