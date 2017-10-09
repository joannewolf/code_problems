#include <algorithm>
class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> result;
        for (int i : nums) {
        	int index = abs(i) - 1;
        	if (nums[index] < 0)
        		result.push_back(index + 1);
        	else
        		nums[index] = -nums[index];
        }
        return result;
    }
};