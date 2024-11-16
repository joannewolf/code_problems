class Solution(object):
    # whether can distribute <= k items to n stores
    def canDistrubute(self, n, quantities, k):
        import math
        sum_n = sum([math.ceil(float(q) / k) for q in quantities])
        return sum_n <= n

    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """
        result = -1
        left, right = 1, max(quantities)
        # when feeding array element to function will return [False, False, ..., True, True]
        # return first element that function return True
        while left <= right:
            mid = (left + right) // 2
            if self.canDistrubute(n, quantities, mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
