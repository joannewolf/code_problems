class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        pattern1, pattern2 = '', ''
        L_index_1, L_index_2 = [], []
        R_index_1, R_index_2 = [], []
        N = len(start)
        for i in range(N):
            if start[i] == 'L':
                pattern1 += 'L'
                L_index_1.append(i)
            elif start[i] == 'R':
                pattern1 += 'R'
                R_index_1.append(i)

            if target[i] == 'L':
                pattern2 += 'L'
                L_index_2.append(i)
            elif target[i] == 'R':
                pattern2 += 'R'
                R_index_2.append(i)

        if pattern1 != pattern2:
            return False

        for i in range(len(L_index_1)):
            if L_index_1[i] < L_index_2[i]:
                return False
        for i in range(len(R_index_1)):
            if R_index_1[i] > R_index_2[i]:
                return False

        return True
