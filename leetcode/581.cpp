class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        if (nums.size() <= 1)
            return 0;
        vector<int> nums2(nums);
        sort(nums2.begin(), nums2.end());
        int front = -1, back = -1;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != nums2[i]) {
                front = i;
                break;
            }
        }
        for (int i = nums.size() - 1; i >= 0; i--) {
            if (nums[i] != nums2[i]) {
                back = i;
                break;
            }
        }
        return (front == -1 && back == -1) ? 0 : (back - front + 1);
    }
};