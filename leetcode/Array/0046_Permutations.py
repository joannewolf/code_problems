# recursion
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        N = len(nums)
        if N == 0:
            return [[]]

        result = []
        for i in range(N):
            subresults = self.permute(nums[:i] + nums[i+1:])
            for subresult in subresults:
                result.append(subresult + [nums[i]])
        return result

# iteration
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        N = len(nums)
        result = [[]]

        # add one num to permutations at a time
        for i in range(N):
            new_result = []
            for permutation in result:
                # insert new num to all intervals
                for j in range(i+1):
                    new_result.append(permutation[:j] + [nums[i]] + permutation[j:])

            result = new_result

        return result
