// by recusrion
class Solution {
public:
	vector<vector<int>> permute(vector<int>& nums) {
		if (nums.size() == 0)
			return vector<vector<int>>(1);

		vector<vector<int>> result;
		for (int i = 0; i < nums.size(); i++) {
			vector<int> newNums(nums);
			newNums.erase(newNums.begin() + i);
			vector<vector<int>> temp = permute(newNums);
			for (vector<int> &t : temp) {
				t.push_back(nums[i]);
				result.push_back(t);
			}
		}
		return result;
	}
};

// by iteration
class Solution {
public:
	vector<vector<int>> permute(vector<int>& nums) {
		vector<vector<int>> result(1);

		for (int i = 0; i < nums.size(); i++) {
			vector<vector<int>> newResult;
			for (vector<int> &permutation : result) {
				permutation.insert(permutation.begin(), nums[i]);
				newResult.emplace_back(permutation);
				for (int j = 0; j < permutation.size() - 1; j++) {
					swap(permutation[j], permutation[j + 1]);
					newResult.emplace_back(permutation);
				}
			}
			result = newResult;
		}
		return result;
	}
};