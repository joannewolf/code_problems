class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int sum = 0, maxSum;
        for (int i = 0; i < k; i++)
            sum += nums[i];
        maxSum = sum;
        for (int i = 0; i < nums.size() - k; i++) {
            sum -= nums[i];
            sum += nums[i + k];
            if (sum > maxSum)
                maxSum = sum;
        }
        return ((double)maxSum / (double)k);
    }
};