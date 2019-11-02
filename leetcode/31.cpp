#include <algorithm>
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        // rearrange to next greater  order
        for (int i = nums.size() - 1; i > 0; i--) {
            if (nums[i] > nums[i - 1]) {
                sort(nums.begin() + i, nums.end());
                for (int j = i; i < nums.size(); j++) {
                    if (nums[j] > nums[i - 1]) {
                        int temp = nums[j];
                        nums[j] = nums[i - 1];
                        nums[i - 1] = temp;
                        break;
                    }
                }
                return;
            }
        }
        // rearrange to lowest order
        for (int i = 0; i < nums.size() / 2; i++) {
            int temp = nums[i];
            nums[i] = nums[nums.size() - 1 - i];
            nums[nums.size() - 1 - i] = temp;
        }
        return;
    }
};