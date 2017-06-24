#include <algorithm>
#include <vector>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> nums2 (nums);
        sort(nums2.begin(), nums2.end());
        int front = 0, end = nums2.size() - 1;
        while (1) {
        	int temp = nums2[front] + nums2[end];
        	if (temp > target)
        		end --;
        	else if (temp < target)
        		front ++;
        	else {
        		vector<int> result;
        		result.push_back( find(nums.begin(), nums.end(), nums2[front]) - nums.begin() );
        		if (nums2[front] == nums2[end])
        			result.push_back( find(nums.begin() + result[0] + 1, nums.end(), nums2[end]) - nums.begin() );
        		else
        			result.push_back( find(nums.begin() , nums.end(), nums2[end]) - nums.begin() );
        		return result;
        	}
        }
    }
};