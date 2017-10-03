class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
    	if (nums.size() == 0)
    		return 0;
    	
    	vector<int> IS;
    	IS.push_back(nums[0]);
    	for (int i = 1; i < nums.size(); i++) {
    		int l = 0, r = IS.size() - 1;
	        while (l <= r) {
	            int mid = (l + r) / 2;
	            if (IS[mid] < nums[i])
	                l = mid + 1;
	            else
	                r = mid - 1;
	        }
	        if (l < IS.size())
	        	IS[l] = nums[i];
	        else
	        	IS.push_back(nums[i]);
    	}
    	return IS.size();
    }
};