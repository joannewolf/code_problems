// backtracking, pass queen coordinates
class Solution {
private:
	int n;
	int putQueens(vector<pair<int, int>> queens) {
		// try to put queens row by row, assume input queens are all valid
		if (queens.size() < n) {
			int result = 0;
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
					result += putQueens(newQueens);
				}
			}
			return result;
		}
		else
			return 1;
	}
public:
	int totalNQueens(int n) {
		this -> n = n;
		int result = 0;

		for (int i = 0; i < n; i++) {
			result += putQueens(vector<pair<int, int>>({make_pair(0, i)}));
		}

		return result;
	}
};

// improved backtracking
class Solution {
private:
	int n;
	int putQueens(vector<int> queens) {
		// try to put queens row by row, assume input queens are all valid
		if (queens.size() < n) {
			int result = 0, queensLen = queens.size();
			vector<bool> valid(n, true);
			for (int i = 0; i < queensLen; i++) {
				valid[queens[i]] = false;
				if (queens[i] - (queensLen - i) >= 0)
					valid[queens[i] - (queensLen - i)] = false;
				if (queens[i] + (queensLen - i) < n)
					valid[queens[i] + (queensLen - i)] = false;
			}

			for (int i = 0; i < n; i++) {
				if (valid[i]) {
					vector<int> newQueens(queens);
					newQueens.emplace_back(i);
					result += putQueens(newQueens);
				}
			}
			return result;
		}
		else
			return 1;
	}
public:
	int totalNQueens(int n) {
		this -> n = n;
		int result = 0;

		for (int i = 0; i < n; i++) 
			result += putQueens(vector<int>({i}));
		
		return result;
	}
};