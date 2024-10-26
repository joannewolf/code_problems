class Solution {
private:
	vector<vector<int>> solve(vector<vector<int>> board) {
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				if (board[i][j] == -1) {
					set<int> candidates({1, 2, 3, 4, 5, 6, 7, 8, 9});

					// check row and column
					for (int k = 0; k < 9; k++) {
						if (board[i][k] != -1 && candidates.find(board[i][k]) != candidates.end())
							candidates.erase(candidates.find(board[i][k]));
						if (board[k][j] != -1 && candidates.find(board[k][j]) != candidates.end())
							candidates.erase(candidates.find(board[k][j]));
					}
					// check sub-box
					for (int k = 0; k < 3; k++) {
						for (int l = 0; l < 3; l++) {
							int temp = board[(i / 3) * 3 + k][(j / 3) * 3 + l];
							if (temp != -1 && candidates.find(temp) != candidates.end())
								candidates.erase(candidates.find(temp));
						}
					}

					// try all candidates
					for (set<int>::iterator it = candidates.begin(); it != candidates.end(); it++) {
						board[i][j] = *it;
						vector<vector<int>> result = solve(board);

						// find if result has empty cell
						bool completed = true;
						for (int k = 0; k < 9; k++) {
							if (find(result[k].begin(), result[k].end(), -1) != result[k].end()) {
								completed = false;
								break;
							}
						}

						if (completed)
							return result;
					}
					return board;
				}
			}
		}
		return board;
	}
public:
    void solveSudoku(vector<vector<char>>& board) {
        vector<vector<int>> numBoard(9, vector<int>(9, -1));
        for (int i = 0; i < 9; i++) {
        	for (int j = 0; j < 9; j++) {
        		if (board[i][j] != '.')
        			numBoard[i][j] = board[i][j] - '0';
        	}
        }

        vector<vector<int>> result = solve(numBoard);
        for (int i = 0; i < 9; i++) {
        	for (int j = 0; j < 9; j++) {
        		board[i][j] = result[i][j] + '0';
        	}
        }
    }
};