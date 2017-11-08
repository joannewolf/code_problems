class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int count = 0;
        map<int, int> sums;
        // sums[i]: number of subarray start from nums[0] which sum == i
        sums[0] = 1;

        int temp = 0;
        for (int n : nums) {
        	temp += n;

        	if (sums.find(temp - k) != sums.end())
        		count += sums[temp - k];

        	if (sums.find(temp) == sums.end())
        		sums[temp] = 1;
        	else
        		sums[temp] ++;
        }

        return count;
    }
};