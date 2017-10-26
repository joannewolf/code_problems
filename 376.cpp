#include <math.h>
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        if (nums.empty())
            return 0;
    	int result = 1, direction = 0;
        // direction, 1: increasing, -1: decreasing
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > nums[i - 1]) {
                if (direction != 1) {
                    result ++;
                }
                direction = 1;
            }
            else if (nums[i] < nums[i - 1]) {
                if (direction != -1) {
                    result ++;
                }
                direction = -1;
            }
        }
        return result;
    }
};