class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if (nums.size() == 0 || target < nums[0])
        	return 0;

        for (int i = 0; i < nums.size() - 1; i++) {
        	if (nums[i] == target)
        		return i;
        	if (nums[i] < target && nums[i + 1] > target)
        		return (i + 1);
        }
        return (nums.back() == target) ? nums.size() - 1 : nums.size();
    }
};