class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        long long product = 1;
        vector<int> result(nums.size(), 0);
        vector<int> zeroIndex;

        for (int i = 0; i < nums.size(); i++) {
        	if (nums[i] == 0)
        		zeroIndex.emplace_back(i);
        	else
        		product *= nums[i];
        }

        if (zeroIndex.size() == 1){
        	result[zeroIndex[0]] = product;
        }
        else if (zeroIndex.size() == 0){
			for (int i = 0; i < nums.size(); i++)
				result[i] = product / nums[i];
        }
        return result;
    }
};