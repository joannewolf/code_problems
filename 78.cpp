#include <math.h>
class Solution {
private:
    vector<vector<int>> combine(vector<int> nums, int k) {
        vector<vector<int>> result;
        if (k == 0)
            result.push_back(vector<int>());
        else if (k == 1) {
            for (int n : nums)
                result.push_back(vector<int>(1, n));
        }
        else {
            for (int i = 0; i < nums.size() - 1; i++) {
                vector<int> nums2(nums.begin() + i + 1, nums.end());
                vector<vector<int>> temp = combine(nums2, k - 1);
                for (vector<int> v : temp) {
                    v.insert(v.begin(), nums[i]);
                    result.push_back(v);
                }
            }
        }
        return result;
    }
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        for (int i = 0; i <= nums.size(); i++) {
            vector<vector<int>> temp = combine(nums, i);
            result.insert(result.end(), temp.begin(), temp.end());
        }
        return result;
    }
};