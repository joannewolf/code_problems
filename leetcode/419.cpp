// without modifying board value
class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        if (board.size() == 0 || board[0].size() == 0)
        	return 0;
        int count = 0, n = board.size(), m = board[0].size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                // count the top-left point of boats
                if (board[i][j] == 'X' && (i == 0 || board[i - 1][j] == '.') && (j == 0 || board[i][j - 1] == '.'))
                    count ++;
            }
        }

        return count;
    }
};

class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        if (board.size() == 0 || board[0].size() == 0)
            return 0;
        int count = 0, n = board.size(), m = board[0].size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 'X') {
                    count ++;
                    int curR = i, curC = j;
                    board[curR][curC] = 'x';
                    while (curR + 1 < n && board[curR + 1][curC] == 'X') {
                        board[curR + 1][curC] = 'x';
                        curR ++;
                    }
                    while (curC + 1 < m && board[curR][curC + 1] == 'X') {
                        board[curR][curC + 1] = 'x';
                        curC ++;
                    }
                }
            }
        }

        return count;
    }
};