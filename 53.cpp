#include <algorithm>
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int result = nums[0], maxLocal = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            maxLocal = max(maxLocal + nums[i], nums[i]);
            result = max(result, maxLocal);
        }
        return result;
    }
};