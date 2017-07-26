#include <stdlib.h>
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int result, distance = 2147483647;
        for (int i = 0; i < nums.size() - 2; i++) {
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
                int temp = nums[i] + nums[l] + nums[r];
                if (abs(temp - target) < distance) {
                    distance = abs(temp - target);
                    result = temp;
                }
                if (temp < target)
                    l ++;
                else
                    r --;
            }
        }

        return result;
    }
};