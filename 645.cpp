class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
    	if (nums.size() == 0)
    		return vector<int>();

        vector<int> result(2, 0);
        int flag = 1;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
        	if (nums[i] != flag) {
        		if (nums[i] == nums[i - 1]) {
        			result[0] = nums[i];
        			flag --;
        		}
        		else {
        			result[1] = flag;
        			flag ++;
        		}
        	}
        	flag ++;
        }
        if (result[1] == 0)
        	result[1] = flag;
        return result;
    }
};