class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        if (nums.size() < 2)
            return -1;
        int slow = nums[0], fast = nums[nums[0]];
        // find circle
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[nums[fast]];
        }
        // find circle's head
        fast = 0;
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }
};