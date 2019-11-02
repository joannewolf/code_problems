// O(N), O(1) space, without division
class Solution {
public:
	vector<int> productExceptSelf(vector<int>& nums) {
		vector<int> result(nums.size());

		// multiply left numbers
		for (int i = 0, temp = 1; i < nums.size(); i++) {
			result[i] = temp;
			temp *= nums[i];
		}

		// multiply right numbers
		for (int i = nums.size() - 1, temp = 1; i >= 0; i--) {
			result[i] *= temp;
			temp *= nums[i];
		}

		return result;
	}
};

// O(N), O(1) space, with division
class Solution {
public:
	vector<int> productExceptSelf(vector<int>& nums) {
		long long product = 1;
		vector<int> result(nums.size(), 0);
		int zeroIndex = -1;

		for (int i = 0; i < nums.size(); i++) {
			if (nums[i] == 0) {
				if (zeroIndex == -1)
					zeroIndex = i;
				else
					return result;
			}
			else
				product *= nums[i];
		}

		if (zeroIndex != -1) {
			result[zeroIndex] = product;
		}
		else {
			for (int i = 0; i < nums.size(); i++)
				result[i] = product / nums[i];
		}
		return result;
	}
};