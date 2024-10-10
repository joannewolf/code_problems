// O(N), bit manipulation
class Solution {
public:
	int singleNumber(vector<int>& nums) {
		int result = 0;
		for (int i = 0; i < nums.size(); i++)
			result ^= nums[i];
		return result;
	}
};

// O(N)
class Solution {
public:
	int singleNumber(vector<int>& nums) {
		set<int> numSet(nums.begin(), nums.end());

		int temp = 0;
		for (auto it = numSet.begin(); it != numSet.end(); it++)
			temp += (2 * *it);
		for (int num : nums)
			temp -= num;

		return temp;
	}
};

// O(NlogN)
class Solution {
public:
	int singleNumber(vector<int>& nums) {
		sort(nums.begin(), nums.end());
		for (int i = 0; i < nums.size() - 1; i += 2) {
			if (nums[i] != nums[i + 1])
				return nums[i];
		}
		return nums.back();
	}
};