class Solution {
private:
    bool existFromHere(vector<vector<char>>& board, int curR, int curC, string word, int flag) {
        if (board[curR][curC] != word[flag])
            return false;
        if (flag == word.length() - 1)
            return true;
        char temp = board[curR][curC];
        board[curR][curC] = -1;

        bool result = ((curR > 0 && existFromHere(board, curR - 1, curC, word, flag + 1))
            || (curR < board.size() - 1 && existFromHere(board, curR + 1, curC, word, flag + 1))
            || (curC > 0 && existFromHere(board, curR, curC - 1, word, flag + 1))
            || (curC < board[0].size() - 1 && existFromHere(board, curR, curC + 1, word, flag + 1)));
        
        board[curR][curC] = temp;
        return result;
    }
public:
    bool exist(vector<vector<char>>& board, string word) {
        if (board.size() == 0 || board[0].size() == 0 || word.length() == 0)
            return false;
        int m = board.size(), n = board[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (existFromHere(board, i, j, word, 0))
                    return true;
            }
        }
        return false;
    }
};