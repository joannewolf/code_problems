// O(N^2), array erasion
class Solution {
public:
	int removeElement(vector<int>& nums, int val) {
		for (int i = 0; i < nums.size(); i++) {
			if (nums[i] == val) {
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
	int removeElement(vector<int>& nums, int val) {
		int slow = 0, fast;
		for (fast = 0; fast < nums.size(); fast++) {
			if (nums[fast] != val) {
				nums[slow] = nums[fast];
				slow ++;
			}
		}
		return slow;
	}
};

// O(N), swap
class Solution {
public:
	int removeElement(vector<int>& nums, int val) {
		int flag = 0, len = nums.size();
		while (flag < len) {
			if (nums[flag] == val) {
				nums[flag] = nums[len - 1];
				len --;
			}
			else
				flag++;
		}
		return len;
	}
};