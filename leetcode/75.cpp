// O(N)
class Solution {
public:
	void sortColors(vector<int>& nums) {
		int j = 0, k = nums.size() - 1;
		for (int i = 0; i <= k; i++) {
			if (nums[i] == 0)
				swap(nums[i], nums[j++]);
			else if (nums[i] == 2)
				swap(nums[i--], nums[k--]);
		}
	}
};

// O(N)
class Solution {
public:
	void sortColors(vector<int>& nums) {
		vector<int> flag(3, 0);
		for (int i = 0; i < nums.size(); i++) {
			int val = nums[i];
			nums.erase(nums.begin() + i);
			nums.insert(nums.begin() + flag[val], val);
			for (int j = val; j <= 2; j++)
				flag[j] ++;
		}
	}
};

// O(2N)
class Solution {
public:
	void sortColors(vector<int>& nums) {
		vector<int> count(3, 0);
		for (int i : nums) {
			count[i] ++;
		}

		for (int i = 0; i < count[0]; i++)
			nums[i] = 0;
		for (int i = count[0]; i < count[0] + count[1]; i++)
			nums[i] = 1;
		for (int i = count[0] + count[1]; i < count[0] + count[1] + count[2]; i++)
			nums[i] = 2;
	}
};