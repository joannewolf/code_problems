class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> result;
        int l = 0, r = nums.size() - 1;
        // find first target
        while (l <= r) {
            int middle = (l + r) / 2;
            if (nums[middle] == target && (middle == 0 || nums[middle - 1] < target)) {
                result.push_back(middle);
                break;
            }
            if (nums[middle] < target)
                l = middle + 1;
            else
                r = middle - 1;
        }
        if (result.size() < 1)
            result.push_back(-1);
        // find last target
        l = 0, r = nums.size() - 1;
        while (l <= r) {
            int middle = (l + r) / 2;
            if (nums[middle] == target && (middle == nums.size() - 1 || nums[middle + 1] > target)) {
                result.push_back(middle);
                break;
            }
            if (nums[middle] > target)
                r = middle - 1;
            else
                l = middle + 1;
        }
        if (result.size() < 2)
            result.push_back(-1);
        return result;
    }
};