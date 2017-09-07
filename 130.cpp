#include <utility>
class Solution {
public:
    void solve(vector<vector<char>>& board) {
        if (board.size() == 0 || board[0].size() == 0)
        	return;

        int n = board.size(), m = board[0].size();
        stack<pair<int, int>> s;

        // find all non-surrounded regions, started with points on edge
        for (int i = 0; i < n; i++) {
        	if (board[i][0] == 'O')
        		s.push(make_pair(i, 0));
        	if (board[i][m - 1] == 'O')
        		s.push(make_pair(i, m - 1));
        }
        for (int i = 0; i < m; i++) {
        	if (board[0][i] == 'O')
        		s.push(make_pair(0, i));
        	if (board[n - 1][i] == 'O')
        		s.push(make_pair(n - 1, i));
        }
        while (!s.empty()) {
        	int curR = s.top().first, curC = s.top().second;
        	s.pop();
        	board[curR][curC] = 'o';
        	if (curR != 0 && board[curR - 1][curC] == 'O')
        		s.push(make_pair(curR - 1, curC));
        	if (curR != n - 1 && board[curR + 1][curC] == 'O')
        		s.push(make_pair(curR + 1, curC));
        	if (curC != 0 && board[curR][curC - 1] == 'O')
        		s.push(make_pair(curR, curC - 1));
        	if (curC != m - 1 && board[curR][curC + 1] == 'O')
        		s.push(make_pair(curR, curC + 1));
        }

        for (int i = 0; i < n; i++) {
        	for (int j = 0; j < m; j++) {
        		if (board[i][j] == 'O')
        			board[i][j] = 'X';
        		else if (board[i][j] == 'o')
        			board[i][j] = 'O';
        	}
        }
    }
};