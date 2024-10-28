class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True

        N, M = len(t), len(s)
        start_candidates = []
        for i in range(N):
            if t[i] == s[0]:
                start_candidates.append(i)

        for start in start_candidates:
            flag_s = 0
            flag_t = start
            while flag_s < M and flag_t < N:
                if t[flag_t] == s[flag_s]:
                    flag_s += 1
                    flag_t += 1
                else:
                    flag_t += 1

            if flag_s == M:
                return True

        return False
