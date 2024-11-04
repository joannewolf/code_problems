class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        N, M = len(s), len(goal)
        if N != M:
            return False

        start_candidates = []
        for j in range(M):
            if goal[j] == s[0]:
                start_candidates.append(j)

        for start in start_candidates:
            all_pass = True
            for i in range(N):
                if s[i] != goal[(start + i) % N]:
                    all_pass = False
                    break
            if all_pass:
                return True

        return False
