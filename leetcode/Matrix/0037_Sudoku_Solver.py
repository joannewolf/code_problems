class Solution(object):
    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    candidate = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
                    # check same row and column
                    for k in range(9):
                        if board[i][k] != '.' and board[i][k] in candidate:
                            candidate.remove(board[i][k])
                        if board[k][j] != '.' and board[k][j] in candidate:
                            candidate.remove(board[k][j])
                    # check sub-box
                    for k in range(3):
                        for l in range(3):
                            i2 = i // 3 * 3 + k
                            j2 = j // 3 * 3 + l
                            if board[i2][j2] != '.' and board[i2][j2] in candidate:
                                candidate.remove(board[i2][j2])

                    # try all candidate
                    if not candidate:
                        return None

                    for num in candidate:
                        board[i][j] = num
                        result = self.solve(board)
                        if result:
                            return result

                    # pass by reference, undo before return
                    board[i][j] = '.'
                    return None

        return board

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.solve(board)
