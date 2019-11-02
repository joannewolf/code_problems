class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        map<int, vector<int>> count; // for every element, record counts, first element index, last element index

        for (int i = 0; i < nums.size(); i++) {
        	if (count.find(nums[i]) == count.end())
        		count[nums[i]] = vector<int>({1, i, i});
        	else {
        		count[nums[i]][0] ++;
        		count[nums[i]][2] = i;
        	}
        }

        int shortestSubarrayLength = 0, maxCount = 0;
        for (auto it = count.begin(); it != count.end(); it++) {
        	if ((it -> second)[0] > maxCount) {
        		maxCount = it -> second[0];
        		shortestSubarrayLength = (it -> second)[2] - (it -> second)[1] + 1;
        	}
        	else if ((it -> second)[0] == maxCount)
        		shortestSubarrayLength = min(shortestSubarrayLength, (it -> second)[2] - (it -> second)[1] + 1);
        }
        return shortestSubarrayLength;
    }
};