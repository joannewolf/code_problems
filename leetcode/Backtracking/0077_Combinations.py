# recursion
class Solution(object):
    def combineNums(self, nums, k):
        if k == 0:
            return [[]]

        N = len(nums)
        result = []
        for i in range(N):
            subresults = self.combineNums(nums[i+1:], k - 1)
            for subresult in subresults:
                subresult.append(nums[i])
                result.append(subresult)

        return result

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        return self.combineNums(list(range(1, n+1)), k)
