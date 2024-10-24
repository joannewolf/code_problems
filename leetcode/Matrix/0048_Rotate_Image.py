class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        start_i, start_j = 0, 0
        end_i, end_j = N - 1, N - 1
        # rotate one circle at a time
        while start_i < end_i and start_j < end_j:
            n = end_i - start_i + 1
            for i in range(n - 1):
                temp = matrix[start_i][start_j + i] # up left
                matrix[start_i][start_j + i] = matrix[end_i - i][start_j] # down left to up left
                matrix[end_i - i][start_j] = matrix[end_i][end_j - i] # down right to down left
                matrix[end_i][end_j - i] = matrix[start_i + i][end_j] # up right to down right
                matrix[start_i + i][end_j] = temp # up left to up right
            start_i += 1
            end_i -= 1
            start_j += 1
            end_j -= 1
