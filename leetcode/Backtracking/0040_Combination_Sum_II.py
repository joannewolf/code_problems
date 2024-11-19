# recursion
class Solution(object):
    def combinationSum2(self, candidates, target):
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
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] <= target:
                subresults = self.combinationSum2(candidates[i+1:], target - candidates[i])
                for subresult in subresults:
                    subresult.append(candidates[i])
                    result.append(subresult)

        return result

# iteration, DP
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = [] # dp[i]: the conbination "index" sum to target i
        for _ in range(target + 1):
            dp.append([])
        dp[0] = [[]]

        N = len(candidates)
        candidates.sort()
        for n in range(1, target + 1):
            for i in range(N):
                if candidates[i] <= n:
                    subresults = dp[n - candidates[i]]
                    # maintain index in combination are ascending, if duplicate num, always save the smaller index
                    for subresult in subresults:
                        if not subresult or i > subresult[-1]:
                            if i == 0 or candidates[i] != candidates[i - 1] or (subresult and subresult[-1] == i - 1):
                                dp[n].append(subresult + [i])
                else:
                    break

        result = []
        for combination in dp[target]:
            result.append([candidates[i] for i in combination])

        return result
