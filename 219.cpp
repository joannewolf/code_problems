#include <map>
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        if (k <= 0)
        	return false;

        map<int, int> pos;
        for(int i = 0; i < nums.size(); i++) {
        	if (pos.find(nums[i]) != pos.end() && i - pos[nums[i]] <= k)
       			// appeared, compare the distance
       			return true;
        	else
    			// add new entry in map, or update the index
    			pos[nums[i]] = i;
        }
        return false;
    }
};