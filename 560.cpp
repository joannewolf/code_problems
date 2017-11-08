class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int count = 0, n = nums.size();
        vector<int> sums(n);
        // sums[i]: sum of numbers from nums[0] to nums[i]

        int temp = 0;
        for (int i = 0; i < n; i++) {
        	temp += nums[i];
        	sums[i] = temp; 
        }

        for (int i = 0; i < n; i++) {
        	if (sums[i] == k)
        		count ++;

        	for (int j = i - 1; j >= 0; j--) {
        		if (sums[i] - sums[j] == k)
        			count ++;
        	}
        }

        return count;
    }
};