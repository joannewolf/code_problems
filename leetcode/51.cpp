// backtracking, pass whole board
class Solution {
private:
	int n;
	vector<vector<string>> putQueens(vector<string> board, pair<int, int> queen) {
		// try to put queens row by row, the input queen coordinate is assumed valid
		// block all invalid places
		for (int i = 0; i < n; i++) {
			board[queen.first][i] = '-';
			board[i][queen.second] = '-';
			if (queen.first - i >= 0 && queen.second - i >= 0)
				board[queen.first - i][queen.second - i] = '-';
			if (queen.first + i < n && queen.second + i < n)
				board[queen.first + i][queen.second + i] = '-';
			if (queen.first - i >= 0 && queen.second + i < n)
				board[queen.first - i][queen.second + i] = '-';
			if (queen.first + i < n && queen.second - i >= 0)
				board[queen.first + i][queen.second - i] = '-';
		}
		board[queen.first][queen.second] = 'Q';

		// go to next row or terminate
		if (queen.first < n - 1) {
			vector<vector<string>> result;
			for (int i = 0; i < n; i++) {
				if (board[queen.first + 1][i] == '.') {
					vector<vector<string>> tempResult = putQueens(board, make_pair(queen.first + 1, i));
					for (vector<string> &temp : tempResult) {
						if (temp.back().find('Q') != -1)
							result.emplace_back(temp);
					}
				}
			}
			return result;
		}
		else
			return vector<vector<string>>({board});
	}
public:
	vector<vector<string>> solveNQueens(int n) {
		this -> n = n;
		vector<vector<string>> result;

		for (int i = 0; i < n; i++) {
			vector<vector<string>> tempResult = putQueens(vector<string>(n, string(n, '.')), make_pair(0, i));
			for (vector<string> &temp : tempResult) {
				if (temp.back().find('Q') != -1) {
					// replace the empty space symbol
					for (int j = 0; j < n; j++) {
						for (int k = 0; k < n; k++) {
							if (temp[j][k] == '-')
								temp[j][k] = '.';
						}
					}
					result.emplace_back(temp);
				}
			}
		}

		return result;
	}
};

// backtracking, pass queen coordinates
class Solution {
private:
	int n;
	vector<vector<pair<int, int>>> putQueens(vector<pair<int, int>> queens) {
		// try to put queens row by row, assume input queens are all valid
		if (queens.size() < n) {
			vector<vector<pair<int, int>>> result;
			for (int i = 0; i < n; i++) {
				// check if (queens.size(), i) is valid to put new queen
				bool valid = true;
				for (int j = 0; j < queens.size(); j++) {
					if (i == queens[j].second || abs(queens.size() - queens[j].first) == abs(i - queens[j].second)) {
						valid = false;
						break;
					}
				}

				if (valid) {
					vector<pair<int, int>> newQueens(queens);
					newQueens.emplace_back(make_pair(queens.size(), i));
					vector<vector<pair<int, int>>> tempResult = putQueens(newQueens);
					for (vector<pair<int, int>> &temp : tempResult) {
						if (temp.size() == n)
							result.emplace_back(temp);
					}
				}
			}
			return result;
		}
		else
			return vector<vector<pair<int, int>>>({queens});
	}
public:
	vector<vector<string>> solveNQueens(int n) {
		this -> n = n;
		vector<vector<string>> result;

		for (int i = 0; i < n; i++) {
			vector<vector<pair<int, int>>> tempResult = putQueens(vector<pair<int, int>>({make_pair(0, i)}));
			for (vector<pair<int, int>> &temp : tempResult) {
				vector<string> board(n, string(n, '.'));
				for (int j = 0; j < n; j++)
					board[temp[j].first][temp[j].second] = 'Q';
				result.emplace_back(board);
			}
		}

		return result;
	}
};