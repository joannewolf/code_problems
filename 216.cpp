class Solution {
private:
	vector<vector<int>> combine(int k, int n, int candidateEnd) {
		vector<vector<int>> result;

		if (n < 0)
			return result;
		if (n == 0)
			return (k == 0) ? vector<vector<int>>(1, vector<int>()) : result;

		for (int i = candidateEnd; i >= 1; i--) {
			if (n >= i) {
				vector<vector<int>> tempResult = combine(k - 1, n - i, i - 1);
				for (vector<int> &vec : tempResult) {
					vec.emplace_back(i);
					result.emplace_back(vec);
				}
			}
		}

		return result;
	}

public:
    vector<vector<int>> combinationSum3(int k, int n) {
        return combine(k, n, 9);
    }
};