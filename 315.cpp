class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
    	int n = nums.size();
        vector<int> sortedNums;
        vector<int> smallerCount(n, 0);

        for (int i = n - 1; i >= 0; i--) {
        	int l = 0, r = sortedNums.size() - 1;
        	while (l <= r) {
        		int middle = (l + r) / 2;
        		if (sortedNums[middle] < nums[i])
        			l = middle + 1;
        		else
        			r = middle - 1;
        	}
        	smallerCount[i] = l;
        	sortedNums.insert(sortedNums.begin() + l, nums[i]);
        }

        return smallerCount;
    }
};