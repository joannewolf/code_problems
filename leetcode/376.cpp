// O(N), greedy
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

// O(N), dynamic programming
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

// O(N^2), dynamic programming
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