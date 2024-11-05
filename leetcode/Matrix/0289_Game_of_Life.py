class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        N, M = len(board), len(board[0])
        neighbors = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if i > 0 and j > 0:
                    neighbors[i][j] += board[i-1][j-1]
                if i > 0:
                    neighbors[i][j] += board[i-1][j]
                if i > 0 and j < M - 1:
                    neighbors[i][j] += board[i-1][j+1]
                if j < M - 1:
                    neighbors[i][j] += board[i][j+1]
                if i < N - 1 and j < M - 1:
                    neighbors[i][j] += board[i+1][j+1]
                if i < N - 1:
                    neighbors[i][j] += board[i+1][j]
                if i < N - 1 and j > 0:
                    neighbors[i][j] += board[i+1][j-1]
                if j > 0:
                    neighbors[i][j] += board[i][j-1]

        for i in range(N):
            for j in range(M):
                if board[i][j] == 1:
                    if neighbors[i][j] < 2 or neighbors[i][j] > 3:
                        board[i][j] = 0
                else:
                    if neighbors[i][j] == 3:
                        board[i][j] = 1
