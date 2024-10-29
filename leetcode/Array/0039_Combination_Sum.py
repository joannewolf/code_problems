# recursion
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if target == 0:
            return [[]]

        N = len(candidates)
        candidates.sort()
        result = []
        for i in range(N):
            if candidates[i] <= target:
                subresults = self.combinationSum(candidates[i:], target - candidates[i])
                for subresult in subresults:
                    subresult.append(candidates[i])
                    result.append(subresult)

        return result

# iteration, DP
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = [] # dp[i]: the conbination sum to target i
        for _ in range(target + 1):
            dp.append([])
        dp[0] = [[]]

        candidates.sort()
        for n in range(1, target + 1):
            for num in candidates:
                if num <= n:
                    subresults = dp[n - num]
                    # maintain nums in combination are ascending
                    for subresult in subresults:
                        if not subresult or num >= subresult[-1]:
                            dp[n].append(subresult + [num])
                else:
                    break

        return dp[target]
