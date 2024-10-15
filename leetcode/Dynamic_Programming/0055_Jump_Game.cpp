class Solution {
public:
    bool canJump(vector<int>& nums) {
        int lastTrue = nums.size() - 1;
        for (int i = nums.size() - 2; i >= 0; i--) {
            if (i + nums[i] >= lastTrue) {
                lastTrue = i;
            }
        }
        return (nums[0] >= lastTrue);
    }
};