// O(N^2), array erasion
class Solution {
public:
	int removeDuplicates(vector<int>& nums) {
		for (int i = 1; i < nums.size(); i++) {
			if (nums[i] == nums[i - 1]) {
				nums.erase(nums.begin() + i);
				i --;
			}
		}
		return nums.size();
	}
};

// O(N), two pointers
class Solution {
public:
	int removeDuplicates(vector<int>& nums) {
		if (nums.size() == 0)
			return 0;

		int slow = 0, fast;
		for (fast = 1; fast < nums.size(); fast++) {
			if (nums[fast] != nums[slow]) {
				slow ++;
				nums[slow] = nums[fast];
			}
		}
		return (slow + 1);
	}
};
