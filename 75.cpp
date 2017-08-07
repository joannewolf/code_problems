class Solution {
public:
    void sortColors(vector<int>& nums) {
        vector<int> flag(3, 0);
        for (int i = 0; i < nums.size(); i++) {
            int val = nums[i];
            nums.erase(nums.begin() + i);
            nums.insert(nums.begin() + flag[val], val);
            for (int j = val; j <= 2; j++)
                flag[j] ++;
        }
    }
};