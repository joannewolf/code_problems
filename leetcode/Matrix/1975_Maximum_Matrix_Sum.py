from unittest import result


class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # Choose any two adjacent elements of matrix and multiply each of them by -1
        # if 2 positive value -> never do action
        # if 1 positive and 1 negative value -> move the minus sign
        # if 2 negative value -> make them all positive
        # if there's 0, move all minus sign to it and make it ineffective
        # if there's no 0, move all minus sign together
        #   if even negative, pair them and make all negative ineffective
        #   if odd negative, only remain one negative and assign to min abs value
        INT_MAX = 1000000
        N, M = len(matrix), len(matrix[0])
        sum_abs = 0
        min_abs = INT_MAX
        is_zero_exist = False
        count_negative = 0
        for i in range(N):
            for j in range(M):
                sum_abs += abs(matrix[i][j])
                min_abs = min(min_abs, abs(matrix[i][j]))
                if matrix[i][j] == 0:
                    is_zero_exist = True
                elif matrix[i][j] < 0:
                    count_negative += 1

        if is_zero_exist or count_negative % 2 == 0:
            result = sum_abs
        else:
            result = sum_abs - 2 * min_abs
        return result
