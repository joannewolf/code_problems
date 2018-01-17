// backtracking, by recursion
class Solution {
public:
	vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
		if (target == 0)
			return vector<vector<int>>({vector<int>()});
		if (candidates.size() == 0 || target < 0)
			return vector<vector<int>>();

		vector<vector<int>> result;
		sort(candidates.begin(), candidates.end());
		for (int i = 0; i < candidates.size(); i++) {
			if (candidates[i] <= target) {
				vector<int> newCandidates(candidates.begin() + i, candidates.end());
				vector<vector<int>> tempResult = combinationSum(newCandidates, target - candidates[i]);
				for (vector<int> &temp : tempResult) {
					temp.push_back(candidates[i]);
					result.push_back(temp);
				}
			}
		}

		return result;
	}
};

// dynamic programming, by iteration
class Solution {
public:
	vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
		vector<vector<vector<int>>> dp(target + 1);
		// dp[i]: the combinations to achieve target = i

		sort(candidates.begin(), candidates.end());
		dp[0] = vector<vector<int>>({vector<int>()});
		for (int i = 1; i <= target; i++) {
			for (int j = 0; j < candidates.size() && candidates[j] <= i; j++) {
				vector<vector<int>> clone(dp[i - candidates[j]]);
				for (vector<int> &temp : clone) {
					if (temp.empty() || candidates[j] <= temp.back()) {
						temp.emplace_back(candidates[j]);
						dp[i].emplace_back(temp);
					}
				}
			}
		}
		return dp[target];
	}
};