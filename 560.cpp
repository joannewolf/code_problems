// O(N)
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

// O(N^2)
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