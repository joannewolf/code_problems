#include <math.h>
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        int n = nums.size();
        for (int i = 0; i < pow(2, n); i++) {
            int temp = i, flag = 0;
            vector<int> v;
            while (temp != 0) {
                if (temp & 1)
                    v.push_back(nums[flag]);
                flag ++;
                temp >>= 1;
            }
            result.push_back(v);
        }

        return result;
    }
};