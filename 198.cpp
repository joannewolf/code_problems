#include <algorithm>
class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 0)
            return 0;
        vector<int> rewards(nums.size(), 0);
        if (nums.size() >= 1)
            rewards[0] = nums[0];
        if (nums.size() >= 2)
            rewards[1] = max(nums[0], nums[1]);
        for (int i = 2; i < nums.size(); i++) {
            rewards[i] = max(rewards[i - 1], nums[i] + rewards[i - 2]);
        }
        return rewards.back();
    }
};