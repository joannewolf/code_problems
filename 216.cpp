// backtracking, by recursion
class Solution {
private:
	vector<vector<int>> combine(int k, int n, int candidateEnd) {
		if (n < 0)
			return vector<vector<int>>();
		if (n == 0)
			return (k == 0) ? vector<vector<int>>({vector<int>()}) : vector<vector<int>>();

		vector<vector<int>> result;
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

// dynamic programming, by iteration
class Solution {
public:
	vector<vector<int>> combinationSum3(int k, int n) {
		vector<vector<vector<int>>> dp(n + 1);
		// dp[i]: the combinations to achieve target = i

		dp[0] = vector<vector<int>>({vector<int>()});
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= 9 && j <= i; j++) {
				vector<vector<int>> clone(dp[i - j]);
				for (vector<int> &temp : clone) {
					if (temp.empty() || j > temp.back()) {
						temp.emplace_back(j);
						dp[i].emplace_back(temp);
					}
				}
			}
		}

		vector<vector<int>> result;
		for (vector<int> &tempResult : dp[n]) {
			if (tempResult.size() == k)
				result.emplace_back(tempResult);
		}

		return result;
	}
};