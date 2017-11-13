class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result(nums.size());

        for (int i = 0, temp = 1; i < nums.size(); i++) {
        	result[i] = temp;
        	temp *= nums[i];
        }

        for (int i = nums.size() - 1, temp = 1; i >= 0; i--) {
        	result[i] *= temp;
        	temp *= nums[i];
        }

        return result;
    }
};