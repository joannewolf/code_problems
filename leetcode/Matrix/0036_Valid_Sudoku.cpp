class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
    	vector<bool> checked(10, false);
        // check every row
        for (int i = 0; i < 9; i++) {
        	for (int j = 0; j < 9; j++) {
        		if (board[i][j] == '.')
        			continue;
        		else if (checked[board[i][j] - '0'])
        			return false;
        		else
        			checked[board[i][j] - '0'] = true;
        	}
        	checked = vector<bool> (10, false);
        }

        // check every column
        for (int i = 0; i < 9; i++) {
        	for (int j = 0; j < 9; j++) {
        		if (board[j][i] == '.')
        			continue;
        		else if (checked[board[j][i] - '0'])
        			return false;
        		else
        			checked[board[j][i] - '0'] = true;
        	}
        	checked = vector<bool> (10, false);
        }

        // check every sub-boxes
        for (int i = 0; i < 3; i++) {
        	for (int j = 0; j < 3; j++) {
        		for (int k = 0; k < 3; k++) {
        			for (int l = 0; l < 3; l++) {
        				if (board[i * 3 + k][j * 3 + l] == '.')
        					continue;
        				else if (checked[board[i * 3 + k][j * 3 + l] - '0'])
		        			return false;
		        		else
		        			checked[board[i * 3 + k][j * 3 + l] - '0'] = true;
        			}
        		}
        		checked = vector<bool> (10, false);
        	}
        }
        return true;
    }
};