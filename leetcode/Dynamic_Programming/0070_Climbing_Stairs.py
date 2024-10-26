class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = [0] * (n + 1) # steps[i] means # of ways to reach index n
        steps[n - 1] = 1 # climb 1 step
        steps[n - 2] = 2 # climb (1, 1) or 2 step
        for i in range(n - 3, -1, -1):
            steps[i] = steps[i + 1] + steps[i + 2]

        return steps[0]
