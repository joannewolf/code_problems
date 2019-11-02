// by recursion, backtracking
class Solution {
private:
	vector<vector<int>> combine(vector<int> nums, int k) {
		// k: desired # of numbers in a subset
		vector<vector<int>> result;
		if (k == 0)
			result.push_back(vector<int>());
		else if (k == 1) {
			for (int n : nums)
				result.push_back(vector<int>(1, n));
		}
		else {
			for (int i = 0; i < nums.size() - 1; i++) {
				vector<int> nums2(nums.begin() + i + 1, nums.end());
				vector<vector<int>> temp = combine(nums2, k - 1);
				for (vector<int> v : temp) {
					v.insert(v.begin(), nums[i]);
					result.push_back(v);
				}
			}
		}
		return result;
	}
public:
	vector<vector<int>> subsets(vector<int>& nums) {
		vector<vector<int>> result;
		for (int i = 0; i <= nums.size(); i++) {
			vector<vector<int>> temp = combine(nums, i);
			result.insert(result.end(), temp.begin(), temp.end());
		}
		return result;
	}
};

// by iteration
class Solution {
public:
	vector<vector<int>> subsets(vector<int>& nums) {
		vector<vector<int>> result(1, vector<int>());
		for (int i = 0; i < nums.size(); i++) {
			vector<vector<int>> cloneResult(result);
			for (vector<int> &vec : cloneResult) {
				vec.push_back(nums[i]);
			}
			result.insert(result.end(), cloneResult.begin(), cloneResult.end());
		}

		return result;
	}
};

// by bit manipulation, find 2^n combinations
class Solution {
public:
	vector<vector<int>> subsets(vector<int>& nums) {
		vector<vector<int>> result;
		int n = nums.size();
		for (int i = 0; i < pow(2, n); i++) {
			int temp = i, flag = 0;
			vector<int> v;
			while (temp != 0) {
				if (temp & 1)
					v.push_back(nums[flag]);
				flag ++;
				temp >>= 1;
			}
			result.push_back(v);
		}

		return result;
	}
};