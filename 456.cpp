#include <stack>
class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        if (nums.size() < 3)
        	return false;

        int n = nums.size(), leftMin = nums[0];
        stack<int> st;
        vector<int> leftMins(n, -1);

        // for every element, find the smallest element on its left side
        leftMins[0] = nums[0];
        for (int i = 1; i < n; i++) {
        	if (nums[i] < leftMin) {
        		leftMin = nums[i];
        		leftMins[i] = leftMin;
        	}
        	else
        		leftMins[i] = leftMin;
        }

        for (int j = n - 1; j >= 0; j--) {
        	if (nums[j] == leftMins[j])
        		continue;
        	while (!st.empty() && st.top() <= leftMins[j])
        		st.pop();
        	if (!st.empty() && st.top() < nums[j])
        		return true;
        	st.push(nums[j]);
        }

        return false;
    }
};