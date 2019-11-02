#include <algorithm>
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        if (nums.size() < 3)
            return result;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() && nums[i] <= 0; i++) {
            if (i != 0 && nums[i] == nums[i - 1])
                continue;
            int l = i + 1, r = nums.size() - 1;
            while (l < r) {
                if (l != i + 1 && nums[l] == nums[l - 1]) {
                    l ++;
                    continue;
                }
                if (r != nums.size() - 1 && nums[r] == nums[r + 1]) {
                    r --;
                    continue;
                }

                if (nums[i] + nums[l] + nums[r] == 0) {
                    vector<int> temp;
                    temp.push_back(nums[i]);
                    temp.push_back(nums[l]);
                    temp.push_back(nums[r]);
                    result.push_back(temp);
                    l ++;
                    r --;
                }
                else if (nums[i] + nums[l] + nums[r] < 0)
                    l ++;
                else
                    r --;
            }
        }
        return result;
    }
};