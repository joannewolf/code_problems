# O(m + n) space
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        N, M = len(matrix), len(matrix[0])
        zero_rows = [False] * N
        zero_columns = [False] * M

        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    zero_rows[i] = True
                    zero_columns[j] = True

        for i in range(N):
            for j in range(M):
                if zero_rows[i] or zero_columns[j]:
                    matrix[i][j] = 0

# O(1) space
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        N, M = len(matrix), len(matrix[0])
        # use first row/column to record zeroes
        first_row_zero, first_column_zero = False, False

        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row_zero = True
                    if j == 0:
                        first_column_zero = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # fill zeroes
        for i in range(1, N):
            for j in range(1, M):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row_zero:
            for j in range(M):
                matrix[0][j] = 0
        if first_column_zero:
            for i in range(N):
                matrix[i][0] = 0
