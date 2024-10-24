class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
    	if (nums.empty())
    		return vector<string>();

    	vector<string> result;
        int flag = nums[0];
        for (int i = 1; i < nums.size(); i++) {
        	if (nums[i] != nums[i - 1] + 1) {
        		if (nums[i - 1] == flag)
        			result.emplace_back(to_string(flag));
        		else
        			result.emplace_back(to_string(flag) + "->" + to_string(nums[i - 1]));
        		flag = nums[i];
        	}
        }
        if (nums.back() == flag)
			result.emplace_back(to_string(flag));
		else
			result.emplace_back(to_string(flag) + "->" + to_string(nums.back()));

        return result;
    }
};