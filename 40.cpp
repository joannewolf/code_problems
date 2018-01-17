// backtracking, by recursion
class Solution {
public:
	vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
		if (target == 0)
			return vector<vector<int>>({vector<int>()});
		if (candidates.size() == 0 || target < 0)
			return vector<vector<int>>();

		vector<vector<int>> result;
		sort(candidates.begin(), candidates.end());
		for (int i = 0; i < candidates.size(); i++) {
			if (i != 0 && candidates[i] == candidates[i - 1])
				continue;
			if (candidates[i] <= target) {
				vector<int> newCandidates(candidates.begin() + i + 1, candidates.end());
				vector<vector<int>> tempResult = combinationSum2(newCandidates, target - candidates[i]);
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
	vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
		vector<vector<vector<int>>> dp(target + 1);
		// dp[i]: the combinations index to achieve target = i

		sort(candidates.begin(), candidates.end());
		dp[0] = vector<vector<int>>({vector<int>()});
		for (int i = 1; i <= target; i++) {
			for (int j = 0; j < candidates.size() && candidates[j] <= i; j++) {
				vector<vector<int>> clone(dp[i - candidates[j]]);
				for (vector<int> &temp : clone) {
					if ((temp.empty() || j > temp.back()) && 
						(j == 0 || candidates[j] != candidates[j - 1] || (!temp.empty() && temp.back() == j - 1))) {
						temp.emplace_back(j);
						dp[i].emplace_back(temp);
					}
				}
			}
		}

		vector<vector<int>> result;
		for (vector<int> &temp : dp[target]) {
			vector<int> tempResult;
			for (int &idx : temp)
				tempResult.emplace_back(candidates[idx]);
			result.emplace_back(tempResult);
		}
		return result;
	}
};