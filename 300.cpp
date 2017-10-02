class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
    	if (nums.size() == 0)
    		return 0;
    	
    	int n = nums.size(), maxLength = 1;
        vector<int> ISlength(n, 1);
        for (int i = 1; i < n; i++) {
        	for (int j = i - 1; j >= 0; j--) {
        		if (nums[i] > nums[j])
        			ISlength[i] = max(ISlength[i], ISlength[j] + 1);
        	}
        	maxLength = max(maxLength, ISlength[i]);
        }
        return maxLength;
    }
};