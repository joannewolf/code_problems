class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        N = len(matrix)
        M = len(matrix[0])
        start_i, start_j = 0, 0
        end_i, end_j = N - 1, M - 1
        result = []
        while start_i <= end_i and start_j <= end_j:
            if start_i == end_i:
                # only one row rectangle
                for j in range(start_j, end_j + 1):
                    result.append(matrix[start_i][j])
                start_i += 1
                end_j -= 1
            elif start_j == end_j:
                # only one column rectangle
                for i in range(start_i, end_i + 1):
                    result.append(matrix[i][start_j])
                start_j += 1
                end_j -= 1
            else:
                # print up row
                for j in range(start_j, end_j + 1):
                    result.append(matrix[start_i][j])
                # print right column
                for i in range(start_i + 1, end_i):
                    result.append(matrix[i][end_j])
                # print bottom row
                for j in range(end_j, start_j - 1, -1):
                    result.append(matrix[end_i][j])
                # print left column
                for i in range(end_i - 1, start_i, -1):
                    result.append(matrix[i][start_j])
                start_i += 1
                end_i -= 1
                start_j += 1
                end_j -= 1

        return result
