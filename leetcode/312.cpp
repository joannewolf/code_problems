#include <math.h>
class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        // dp[i][j]: in subarray nums[i] to nums[j], choose one element as the last element to pop out
        // the value will be the maximum coins it can get
        vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));
        nums.insert(nums.begin(), 1);
        nums.insert(nums.end(), 1);

        for (int range = 1; range <= n; range ++) {
        	for (int left = 1; left <= n - range + 1; left ++) {
        		int right = left + range - 1, maxCoin = 0;
        		// int subarray nums[left] to nums[right], try all element as the last element be popped out
        		for (int i = left; i <= right; i++) {
        			int temp = dp[left][i - 1] + dp[i + 1][right] + nums[left - 1] * nums[i] * nums[right + 1];
        			maxCoin = max(maxCoin, temp);
        		}
        		dp[left][right] = maxCoin;
        	}
        }
        return dp[1][n];
    }
};