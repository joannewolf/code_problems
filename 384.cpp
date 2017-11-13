class Solution {
private:
	vector<int> nums;
	int n;
public:
	Solution(vector<int> nums) {
		this -> nums = nums;
		n = nums.size();
	}
	
	/** Resets the array to its original configuration and return it. */
	vector<int> reset() {
		return nums;
	}
	
	/** Returns a random shuffling of the array. */
	vector<int> shuffle() {
		// https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
		vector<int> clone(nums);
		for (int i = 0; i < n; i++) {
			int flag = rand() % (n - i) + i;
			int temp = clone[i];
			clone[i] = clone[flag];
			clone[flag] = temp;
		}
		return clone;
	}
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * vector<int> param_1 = obj.reset();
 * vector<int> param_2 = obj.shuffle();
 */