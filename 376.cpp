#include <math.h>
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
    	if (nums.empty())
    		return 0;
    	int n = nums.size();
        vector<int> dpUp(n, 1), dpDown(n, 1);
        // dpUp[i]: the maximum wiggle length from nums[0] to nums[i], which the last step is wiggle up to nums[i]
        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1]) {
                dpUp[i] = dpDown[i - 1] + 1;
                dpDown[i] = dpDown[i - 1];
            }
            else if (nums[i] < nums[i - 1]) {
                dpDown[i] = dpUp[i - 1] + 1;
                dpUp[i] = dpUp[i - 1];
            }
            else {
                dpUp[i] = dpUp[i - 1];
                dpDown[i] = dpDown[i - 1];
            }
        }
        
        return max(dpUp[n - 1], dpDown[n - 1]);
    }
};