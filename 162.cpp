#include <climits>
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
    	nums.insert(nums.begin(), INT_MIN);
    	nums.insert(nums.end(), INT_MIN);
        int l = 1, r = nums.size() - 2;
        while (l <= r) {
        	int middle = (l + r) / 2;
        	if (nums[middle - 1] <= nums[middle] && nums[middle] >= nums[middle + 1])
        		return (middle - 1);
        	else if (nums[middle - 1] <= nums[middle] && nums[middle] <= nums[middle + 1])
        		l = middle + 1;
        	else
        		r = middle - 1;
        }
    }
};