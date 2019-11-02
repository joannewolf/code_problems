class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() <= 1)
            return nums.size();

        int count = 1;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == nums[i - 1]) {
                if (count < 2)
                    count ++;
                else {
                    nums.erase(nums.begin() + i);
                    i --;
                }
            }
            else
                count = 1;
        }
        return nums.size();
    }
};