class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check rows
        for i in range(9):
            num_set = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in num_set:
                        return False
                    else:
                        num_set.add(board[i][j])

        # check columns
        for j in range(9):
            num_set = set()
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in num_set:
                        return False
                    else:
                        num_set.add(board[i][j])

        # check 3 * 3 sub-box
        for i in range(3):
            for j in range(3):
                num_set = set()
                sub_board = [
                    board[i * 3][j * 3], board[i * 3 + 1][j * 3], board[i * 3 + 2][j * 3],
                    board[i * 3][j * 3 + 1], board[i * 3 + 1][j * 3 + 1], board[i * 3 + 2][j * 3 + 1],
                    board[i * 3][j * 3 + 2], board[i * 3 + 1][j * 3 + 2], board[i * 3 + 2][j * 3 + 2],
                ]
                for char in sub_board:
                    if char != '.':
                        if char in num_set:
                            return False
                        else:
                            num_set.add(char)

        return True