#include <math.h>
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
    	if (nums.empty())
    		return 0;
    	int n = nums.size();
        vector<int> dp(n, 1); // dp[i]: the maximum wiggle length from nums[0] to nums[i]
        vector<int> direction(n, 0);

        for (int i = 1; i < n; i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (nums[i] > nums[j] && direction[j] != 1 && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    direction[i] = 1;
                }
                if (nums[i] < nums[j] && direction[j] != -1 && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    direction[i] = -1;
                }
            }
        }
        return dp[n - 1];
    }
};