#include <utility>
class Solution {
public:
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        if (board[click[0]][click[1]] == 'M') {
        	board[click[0]][click[1]] = 'X';
        	return board;
        }

        int n = board.size(), m = board[0].size();
    	stack<pair<int, int>> st;
    	st.push(make_pair(click[0], click[1]));
    	while (!st.empty()) {
    		pair<int, int> curPos = st.top();
    		st.pop();
    		if (board[curPos.first][curPos.second] != 'E')
    			continue;

    		int mineCount = 0;
    		// count adjacent mines
    		if (curPos.first != 0 && board[curPos.first - 1][curPos.second] == 'M')
    			mineCount ++;
  			if (curPos.first != 0 && curPos.second != m - 1 && board[curPos.first - 1][curPos.second + 1] == 'M')
    			mineCount ++;
    		if (curPos.second != m - 1 && board[curPos.first][curPos.second + 1] == 'M')
    			mineCount ++;
    		if (curPos.first != n - 1 && curPos.second != m - 1 && board[curPos.first + 1][curPos.second + 1] == 'M')
    			mineCount ++;
    		if (curPos.first != n - 1 && board[curPos.first + 1][curPos.second] == 'M')
    			mineCount ++;
    		if (curPos.first != n - 1 && curPos.second != 0 && board[curPos.first + 1][curPos.second - 1] == 'M')
    			mineCount ++;
    		if (curPos.second != 0 && board[curPos.first][curPos.second - 1] == 'M')
    			mineCount ++;
    		if (curPos.first != 0 && curPos.second != 0 && board[curPos.first - 1][curPos.second - 1] == 'M')
    			mineCount ++;

    		if (mineCount != 0)
    			board[curPos.first][curPos.second] = mineCount + 48;
    		else {
    			board[curPos.first][curPos.second] = 'B';
				if (curPos.first != 0 && board[curPos.first - 1][curPos.second] == 'E')
	    			st.push(make_pair(curPos.first - 1, curPos.second));
	  			if (curPos.first != 0 && curPos.second != m - 1 && board[curPos.first - 1][curPos.second + 1] == 'E')
	    			st.push(make_pair(curPos.first - 1, curPos.second + 1));
	    		if (curPos.second != m - 1 && board[curPos.first][curPos.second + 1] == 'E')
	    			st.push(make_pair(curPos.first, curPos.second + 1));
	    		if (curPos.first != n - 1 && curPos.second != m - 1 && board[curPos.first + 1][curPos.second + 1] == 'E')
	    			st.push(make_pair(curPos.first + 1, curPos.second + 1));
	    		if (curPos.first != n - 1 && board[curPos.first + 1][curPos.second] == 'E')
	    			st.push(make_pair(curPos.first + 1, curPos.second));
	    		if (curPos.first != n - 1 && curPos.second != 0 && board[curPos.first + 1][curPos.second - 1] == 'E')
	    			st.push(make_pair(curPos.first + 1, curPos.second - 1));
	    		if (curPos.second != 0 && board[curPos.first][curPos.second - 1] == 'E')
	    			st.push(make_pair(curPos.first, curPos.second - 1));
	    		if (curPos.first != 0 && curPos.second != 0 && board[curPos.first - 1][curPos.second - 1] == 'E')
	    			st.push(make_pair(curPos.first - 1, curPos.second - 1));
    		}
    	}
        return board;
    }
};