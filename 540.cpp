class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
    	if (nums.size() == 1)
    		return nums[0];

        int l = 0, r = nums.size() - 1, n = nums.size();
        while (n > 3) {
        	int mid = (l + r) / 2;
        	if (nums[mid] != nums[mid - 1] && nums[mid] != nums[mid + 1])
        		return nums[mid];

        	if (n % 4 == 3) {
        		if (nums[mid] == nums[mid - 1])
        			l = mid + 1;
        		else
        			r = mid - 1;
        		n -= (n / 2 + 1);
        	}
        	else if (n % 4 == 1) {
        		if (nums[mid] == nums[mid - 1])
        			r = mid;
        		else
        			l = mid;
        		n -= (n / 2);
        	}
        }
        return (nums[l] != nums[l + 1]) ? nums[l] : nums[r];
    }
};