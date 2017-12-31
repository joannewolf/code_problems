// without extra space
// when find a number i, flip the number at position i-1 to negative
// if the number at position i-1 is already negative, i is the number that occurs twice
class Solution {
public:
	vector<int> findDuplicates(vector<int>& nums) {
		vector<int> result;
		for (int i : nums) {
			int index = abs(i) - 1;
			if (nums[index] < 0)
				result.push_back(index + 1);
			else
				nums[index] = -nums[index];
		}
		return result;
	}
};

// without extra space
class Solution {
public:
	vector<int> findDuplicates(vector<int>& nums) {
		vector<int> result;
		int i = 0;
		while (i < nums.size()) {
			if (nums[i] != nums[nums[i] - 1])
				swap(nums[i], nums[nums[i] - 1]);
			else
				i++;
		}
		for (i = 0; i < nums.size(); i++) {
			if (nums[i] != i + 1) result.push_back(nums[i]);
		}
		return result;
	}
};

// O(N) space
class Solution {
public:
	vector<int> findDuplicates(vector<int>& nums) {
		vector<int> result, checked(nums.size() + 1, 0);
		for (int i : nums) {
			if (checked[i] != 0)
				result.push_back(i);
			checked[i] ++;
		}

		return result;
	}
};