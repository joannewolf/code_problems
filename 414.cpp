#include <climits>
class Solution {
public:
    int thirdMax(vector<int>& nums) {
        int first = INT_MIN, second = INT_MIN, third = INT_MIN;
        bool intMinExist = false;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == INT_MIN)
                intMinExist = true;
            if (nums[i] == first || nums[i] == second || nums[i] == third)
                continue;
            if (nums[i] > first) {
                third = second;
                second = first;
                first = nums[i];
            }
            else if (nums[i] > second) {
                third = second;
                second = nums[i];
            }
            else if (nums[i] > third)
                third = nums[i];
        }

        return ((intMinExist && first != INT_MIN && second != INT_MIN) || third != INT_MIN) ? third : first;
    }
};