// O(NlogN), use sorting
class Solution {
public:
	bool containsDuplicate(vector<int>& nums) {
		if (nums.empty())
			return false;
		sort(nums.begin(), nums.end());
		for (int i = 1; i < nums.size(); i++) {
			if (nums[i] == nums[i - 1])
				return true;
		}
		return false;
	}
};

// O(N), use set
class Solution {
public:
	bool containsDuplicate(vector<int>& nums) {
		unordered_set<int> set;
		for (int num : nums) {
			if (set.find(num) != set.end())
				return true;
			set.insert(num);
		}
		return false;
	}
};

