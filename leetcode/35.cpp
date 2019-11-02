// O(logN)
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (nums[mid] == target)
                return mid;
            else if (nums[mid] < target)
                l = mid + 1;
            else
                r = mid - 1;
        }
        return l;
    }
};

// O(N)
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if (nums.size() == 0 || target < nums[0])
            return 0;

        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums[i] == target)
                return i;
            if (nums[i] < target && nums[i + 1] > target)
                return (i + 1);
        }
        return (nums.back() == target) ? nums.size() - 1 : nums.size();
    }
};